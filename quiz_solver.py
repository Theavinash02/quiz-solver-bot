# quiz_solver.py
import asyncio
import re
import json
import httpx
from playwright.async_api import async_playwright
from openai import AsyncOpenAI
from config import OPENAI_API_KEY

# Initialize OpenAI
aclient = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def get_llm_answer(question_text):
    """
    Uses OpenAI to parse the question and find the answer logic.
    """
    print("[LLM] Asking OpenAI...")
    system_prompt = """
    You are a quiz solver. Extract the answer or action.
    If it is a direct answer, return JSON: {"answer": <value>}.
    """
    try:
        response = await aclient.chat.completions.create(
            model="gpt-4o-mini", # Or gpt-3.5-turbo
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question_text}
            ],
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        print(f"[LLM Error] {e}")
        return None

async def process_page(client, browser_context, email, secret, current_url):
    page = await browser_context.new_page()
    try:
        print(f"\n[Link] Visiting: {current_url}")
        await page.goto(current_url, wait_until="networkidle")
        
        # 1. Extract Text (Handling atob hidden content)
        try:
            # Wait for the #result div which usually holds the decoded text
            await page.wait_for_selector("#result", state="attached", timeout=10000)
            full_text = await page.locator("#result").inner_text()
            print(f"[Question] {full_text[:100]}...")
        except:
            full_text = await page.locator("body").inner_text()

        # 2. Solve (Try LLM directly)
        answer = None
        llm_result = await get_llm_answer(full_text)
        if llm_result and "answer" in llm_result:
            answer = llm_result["answer"]
        
        # 3. Determine Submit URL
        # Heuristic: append /submit if not explicitly found
        submit_url = current_url.rsplit('/', 1)[0] + "/submit"
        
        # 4. Submit
        payload = {
            "email": email, 
            "secret": secret, 
            "url": current_url, 
            "answer": answer
        }
        print(f"[Submit] {payload}")
        resp = await client.post(submit_url, json=payload)
        return resp.json()

    except Exception as e:
        print(f"[Error] {e}")
        return {"correct": False, "url": None}
    finally:
        await page.close()

async def start_quiz_chain(email: str, secret: str, initial_url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        async with httpx.AsyncClient() as client:
            next_url = initial_url
            while next_url:
                data = await process_page(client, context, email, secret, next_url)
                if data.get("correct") and not data.get("url"):
                    break # Done
                next_url = data.get("url") 
        await browser.close()