import random
import time


from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [{"user": random.choice(["What is Q-drop?", "Are you stuck at populating Review"])}],
                "approach": "rrr",
                "overrides": {"retrieval_mode": "hybrid", "semantic_ranker": True, "semantic_captions": False, "top": 3, "suggest_followup_questions": False},
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [
                    {
                        "user": "What is Q-drop??",
                        "bot": "The solution is developed which implements automation by having a Database integrated solution, a Tool/ Widget to perform QA validations both for Ipro Ecapture and Relativity Checks [Q.pdf].",
                    },
                    {"user": "Does it have limitations?"},
                ],
                "approach": "rrr",
                "overrides": {"retrieval_mode": "hybrid", "semantic_ranker": True, "semantic_captions": False, "top": 3, "suggest_followup_questions": False},
            },
        )
