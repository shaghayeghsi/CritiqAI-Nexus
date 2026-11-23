class MockLLMProvider:
    def classify(self,text):
        t=text.lower()
        if any(w in t for w in ["password","login","access","account"]): return {"category":"account_access","priority":"high"}
        if any(w in t for w in ["course","lecture","assignment","grade"]): return {"category":"academic","priority":"normal"}
        return {"category":"general","priority":"normal"}
    def respond(self,text):
        return ("Thanks for contacting support. Your request has been recorded. "
                "Please try the relevant self-service steps; if the issue continues, the team will review it.")
def get_provider(): return MockLLMProvider()
