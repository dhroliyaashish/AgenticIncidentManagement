def classify_incident(state):
    
    description = state["description"].lower()

    if "login" in description or "authentication" in description:
        category = "Authentication"

    elif "database" in description or "sql" in description:
        category = "Database"

    elif "500" in description or "server error" in description:
        category = "Application"

    else:
        category = "General"

    if state["business_impact"] == "CRITICAL":
        severity = "CRITICAL"

    elif state["affected_users"] > 100:
        severity = "HIGH"

    elif state["affected_users"] > 20:
        severity = "MEDIUM"

    else:
        severity = "LOW"

    return {
        "category": category,
        "severity": severity
    }

def investigate_incident(state):

    category = state["category"]

    root_causes = {
        "Authentication": "Possible identity provider failure",
        "Database": "Possible database connectivity or query issue",
        "Application": "Possible application exception or server-side failure",
        "General": "Insufficient information to identify root cause"
    }

    return {
        "possible_root_cause": root_causes.get(category)
    }

def recommend_solution(state):

    category = state["category"]

    recommendations = {
        "Authentication": [
            "Check identity provider health",
            "Review authentication service logs",
            "Check recent authentication deployments"
        ],

        "Database": [
            "Check database connectivity",
            "Review SQL server logs",
            "Check database connection pool"
        ],

        "Application": [
            "Review application logs",
            "Check recent deployments",
            "Verify application server health"
        ],

        "General": [
            "Collect additional diagnostic information",
            "Review application logs"
        ]
    }

    escalation = (
        state["severity"] in ["HIGH", "CRITICAL"]
    )

    return {
        "recommended_actions": recommendations[category],
        "assigned_team": (
            "Application Support"
            if category != "Database"
            else "Database Support"
        ),
        "escalation_required": escalation,
        "status": "PENDING_APPROVAL" if escalation else "OPEN"
    }