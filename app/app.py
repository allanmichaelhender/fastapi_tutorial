from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "Cool post"},
    2: {"title": "Django Ninja 101", "content": "FastAPI-like documentation for your Django projects."},
    3: {"title": "Python Performance", "content": "Comparing speed differences between Pydantic v1 and v2."},
    4: {"title": "The Art of Async", "content": "How to handle background tasks effectively in modern web apps."},
    5: {"title": "Travel Tips: Japan", "content": "Essential phrases and hidden spots in Kyoto and Osaka."},
    6: {"title": "Morning Routine", "content": "Starting your day with focus: meditation, water, and movement."},
    7: {"title": "React vs Vue in 2025", "content": "Choosing the right frontend framework for your next MVP."},
    8: {"title": "Homemade Sourdough", "content": "A beginner's guide to maintaining a starter and baking bread."},
    9: {"title": "Cybersecurity Basics", "content": "Protecting your data with 2FA and password managers."},
    10: {"title": "Minimalist Workspace", "content": "Setting up a desk that inspires productivity and calm."},
    11: {"title": "Understanding GPT-5", "content": "A deep dive into the latest advancements in large language models."},
    12: {"title": "Running Your First 5K", "content": "A 12-week training plan for absolute beginners."},
    13: {"title": "Dark Mode Best Practices", "content": "Designing UI that is accessible and easy on the eyes."},
    14: {"title": "The Future of Remote Work", "content": "Why hybrid models are winning in the tech industry."},
    15: {"title": "Garden to Table", "content": "Growing your own herbs: basil, rosemary, and mint guide."},
    16: {"title": "Building a Portfolio", "content": "How to showcase your coding projects to get hired."},
    17: {"title": "Financial Literacy", "content": "Understanding the power of compound interest and ETFs."},
    18: {"title": "Space Exploration", "content": "The latest updates on the Mars settlement mission missions."},
    19: {"title": "Mindful Coding", "content": "Techniques for preventing burnout in high-stress dev roles."},
    20: {"title": "Tailwind CSS Tips", "content": "Writing cleaner utility classes using @apply and theme extensions."}
}


@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)
