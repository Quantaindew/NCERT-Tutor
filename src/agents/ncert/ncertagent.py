from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import requests

class Question(Model):
    question: str
    chapter: int
    subject: int
    standard: int

class Text(Model):
    pdf: str
    success: bool
    question: str
    chapter: str
    subject: str
    standard: str


ncert = Agent(
    name="ncert",
    port=8000,
    seed="sigmar secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(ncert.wallet.address())



@ncert.on_event("startup")
async def startup_handler(ctx: Context):
    ctx.logger.info("NCERT Agent Started")
    ctx.logger.info(f"{ncert.address}")

@ncert.on_query(model=Question)
async def question_handler(ctx: Context, sender: str, query: Question):
    try:
        api_url = "https://ncert-tutor-dev-dbkt.3.us-1.fl0.io/send-pdf-content"
        payload = {
            "standard": query.standard,
            "subject": query.subject,
            "chapter": query.chapter,
        }
        response = await requests.post(api_url, json=payload)
        data = response.json()
        sender = ""
        ctx.send(sender, Text(pdf=data, success=True, question=query.question, chapter=query.chapter, subject=query.subject, standard=query.standard))
    except Exception as e:
        ctx.send(sender, Text(pdf=str(e), success=False))

if __name__ == "__main__":
    ncert.run()