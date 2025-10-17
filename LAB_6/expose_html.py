import fastapi
import uvicorn
from fastapi.responses import HTMLResponse

app = fastapi.FastAPI()

@app.get("/dummy_html")
def get_dummy_html():
    var = 12
    return HTMLResponse(content=f"<html><body><h1>This is a dummy HTML {var} response</h1></body></html>", status_code=200)

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("templates/template.html",mode='r', encoding="utf-8") as f:
        html_content = f.read()
    return html_content

@app.get("/euler", response_class=HTMLResponse)
def read_euler():
    with open("templates/euler.html",mode='r', encoding="utf-8") as f:
        # Read the HTML content of the file
        html_content = f.read()
    return html_content

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)