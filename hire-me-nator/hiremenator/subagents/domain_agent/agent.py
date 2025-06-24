from google.adk.agents import Agent

from google.adk.tools.agent_tool import AgentTool
from hiremenator.tools.googlesearch.agent import googlesearch
from hiremenator.tools.googledomain.agent import googledomain

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Any  

class cvdomainskillschema(BaseModel):
    response_to_user: str = Field(
        description=(
            "A conversational response to the user. This should: "
            "1. Acknowledge the CV analysis for domain suggestion. "
            "2. Present the initial suggested career domains/roles/industries. "
            "3. Ask for the user's feedback, preferences, or any specific domains they are considering. "
            "4. If a domain is selected/confirmed, confirm this with the user. "
            "Example: 'Based on your latest CV, I see strong potential in areas like [Domain A] and [Domain B] due to your [specific skills/experience]. "
            "Do any of these align with your interests, or do you have other domains in mind? ... "
            "Okay, so you're interested in focusing on [Selected Domain]. That's a great choice!'"
        )
    )

    suggested_domains: str = Field(        
        description=(
            '''
            
            suggested by the AI based on the analysis of the user's CV.
            A list of career, treding, future trend and in demand domains, industries, or specific job roles initially "
            suggest in structured format and provide a salary, brief description, additional skill and exp needed (that user doesnt have as of now as per the cv), rationale for each suggestion, linking it to the user's skills, experience, or career goals.

            Example strcture:

            Candidate Summary (from CV Analysis)
            Education: M.Sc. in Computer Science

            Experience: 3+ years in Data Analysis

            Skills: Python, SQL, Power BI, Tableau, Machine Learning (basic), Statistical Analysis

            Career Goal (inferred): Growth in analytics, emerging tech, or decision-making roles

            1. Domain: Data Science
            Job Roles: Data Scientist, Machine Learning Engineer, Predictive Modeler

            Avg. Salary (USD): $90,000 – $130,000

            Description: Use statistical models and machine learning techniques to extract insights and forecast trends from complex datasets.

            Rationale: Strong foundation in Python and data analysis makes transition to data science feasible. Add ML and model deployment experience to increase marketability.

            Industry Demand: High — used across finance, health, e-commerce, and more.

            additional skills needed: Machine Learning, Model Deployment

            💡 2. Domain: Business Intelligence & Analytics
            Job Roles: BI Analyst, Analytics Consultant, Dashboard Developer

            Avg. Salary (USD): $75,000 – $110,000

            Description: Focus on gathering business data and presenting insights using tools like Power BI/Tableau.

            Rationale: Candidate has strong dashboarding and SQL skills; aligning with BI ensures short-term job fit and long-term growth.

            Future Outlook: Increasing demand in companies embracing data-driven decision-making.
            additional skills needed: Advanced SQL, Data Warehousing

            🌐 3. Domain: Product/Data Strategy (Tech Industry)
            Job Roles: Data Strategist, Product Analyst, Technical Product Manager

            Avg. Salary (USD): $95,000 – $140,000

            Description: Work at the intersection of data, technology, and business. Use data to influence product direction and strategy.

            Rationale: The analytical background combined with business awareness and communication skills makes this a suitable growth path.

            Trend: High growth — especially in tech startups and data-driven enterprises.
            additional skills needed: Product Management, Stakeholder Communication

            📈 4. Domain: Generative AI & LLM Applications
            Job Roles: AI Product Analyst, Prompt Engineer, LLM App Developer

            Avg. Salary (USD): $110,000 – $150,000

            Description: Design and optimize AI-powered applications using large language models. Involves prompt tuning, data curation, and app logic.

            Rationale: Knowledge of Python + interest in AI/ML + analytical thinking is a strong foundation. Can pivot with some upskilling.

            Future Outlook: Explosive growth; foundational AI roles are highly in demand.]

            additional skills needed: Prompt Engineering, LLM Fine-tuning

            💼 5. Domain: Financial Technology (FinTech) Analytics
            Job Roles: Risk Analyst, Fraud Detection Analyst, FinTech Data Analyst

            Avg. Salary (USD): $85,000 – $120,000

            Description: Analyze financial data to detect fraud, optimize risk models, or create customer insights.

            Rationale: SQL and statistical analysis are crucial in FinTech; with experience, this domain offers a highly rewarding path.

            Industry Growth: FinTech startups and digital banks are booming globally.

            🧠 6. Domain: Health Tech Analytics
            Job Roles: Clinical Data Analyst, Health Informatics Specialist, Healthcare AI Analyst

            Avg. Salary (USD): $80,000 – $115,000

            Description: Use analytics to improve healthcare outcomes, hospital efficiency, and treatment personalization.

            Rationale: Healthcare is increasingly driven by data. The candidate's analytical skills can easily transition into this domain with domain-specific upskilling.

            Future Trend: Aging population + AI in health = sustained demand.
            additional skills needed: Health Informatics, Clinical Data Analysis
            '''
        )
    )


    cvskill_analysis: str = Field(
        ...,
        description='''Full markdown-formatted gap analysis report with skills, projects, tools, suggestions.",
        examples
        """### 🔍 Domain Target: **Data Science**

        ---

        ### 📌 Candidate Summary
        - **Education**: B.Sc. Computer Engineering
        - **Experience**: 2 years as Data Analyst (Retail)
        - **Skills**: Python, SQL, Excel, Power BI
        - **Projects**: Forecasting dashboard, K-means clustering
        - **Certifications**: Google Data Analytics

        ---

        ### 🧠 Skill & Experience Alignment

        | Category                  | Status             | Notes |
        |---------------------------|--------------------|-------|
        | Core Skills               | ⚠️ Partial          | Python & SQL strong; missing ML libraries |
        | Project Experience        | ✅ Relevant         | Clustering good, no model deployment      |
        | Tools & Frameworks        | ❌ Missing          | No TensorFlow, Git, Streamlit             |
        | Certifications            | ✅ Foundational     | Google cert is a good start               |
        | Portfolio                 | ❌ Missing          | No GitHub or public work shared           |

        ---

        ### 🚧 Skill Gaps
        - ❌ TensorFlow, scikit-learn
        - ❌ Model deployment (Flask, Streamlit)
        - ⚠️ Statistics (needs depth)

        ### 🔧 Tool Gaps
        - Git
        - Docker (optional but recommended)

        ### 📂 Project Gaps
        - No deployed models
        - No public proof-of-work

        ### 🧾 Certifications (Recommended)
        - IBM Data Science or AWS ML

        ### 🔄 Action Plan
        1. **Take ML courses (Coursera – Andrew Ng)** ✅
        2. **Build and deploy ML project on GitHub** ✅
        3. **Improve statistics & evaluation skills** ✅
        4. **Learn Git and deployment tools** ⚠️

        ---

        ### 📚 Suggested Courses
        - **ML**: Coursera ML by Andrew Ng
        - **Deployment**: Streamlit + Flask (Docs, Tutorials)
        - **Statistics**: HarvardX (edX)

        ---

        ### 🧭 Next Steps
        Would you like me to help shortlist some courses or tailor your resume next?"""
                '''
    )
    comment: Optional[str] = Field(
        None,
        description='''Optional internal note for orchestration or agent routing. Not shown to user.",
        "Candidate shows moderate readiness for DS roles. Recommend routing to cvresume once GitHub is added.'''
    )

domain_agent = Agent(
    model='gemini-2.0-flash-001',
    name='domain_agent',
    description='''The domain_agent analyzes a user's CV, skills, and experience to identify the most suitable career domains, perform a gap analysis, and recommend an action plan.
     It aligns the user's background with in-demand roles, identifies missing competencies, and suggests courses, certifications, and projects to bridge the gaps. 
    ''',
    instruction='''

### 🧠 Agent Role

* Identify 3–5 best-fit domains from the user’s CV and preferences.
* Match user profile with domain skill/experience trends.
* Perform deep gap analysis and skill mapping.
* Recommend personalized learning paths, certifications, tools, and projects.
* Use external tools to validate demand and future trends.
* Include detailed metadata and sources for transparency.
* If the data is too large to be displayed at once, present the data in chunks untill you present the entire data

---

### 🔄 Thought Process

1. Parse CV and extract experience, education, skills, projects.
2. If domain unclear, consult `root_agent` or `career_advisor_agent`.
3. Use preloaded templates + real-time tools (`google_domain_agent`) to:

   * Match CV with top domains
   * Explore skill benchmarks, future scope, growth trends
   * Assess alignment and identify gaps
4. Ensure all recommendations are evidence-backed and sources are listed.
5. Present concise, structured, explainable suggestions to the user.
6. If the data is too large to be displayed at once, present the data in chunks untill you present the entire data

---

### 🤝 Multi-Agent Request / Coordination

* `cv_agent` → for resume parsing
* `job_analysis_agent` → for domain-level job role expectations
* `google_domain_agent` → for trends, required skills, toolchains
* `career_advisor_agent` → for long-term career pathing
* `news_opportunity_agent` → for courses, internships, events

---

### 💬 User Interactions

* Ask user for preferences or target domains if not specified
* Clarify career goals: growth vs switch vs exploration
* Provide explanations without jargon
* Encourage questions and domain comparison
* Offer to follow up with job search or resume tailoring

---

### 📥 Inputs

* Parsed CV data (from `cv_agent`)
* User-stated preferences (optional)
* Tool-based insights from `google_domain_agent` and `google_search_tool`

---

### ⚙️ Process

1. **CV Parsing**

   * Pull data: education, roles, projects, tools, skills, certifications
   * Detect implicit themes and domain overlaps

2. **Domain Mapping**

   * Suggest 3–5 high-fit domains based on:
     • Alignment to CV
     • Market demand
     • Learning feasibility

3. **External Validation**

   * Use `google_domain_agent` for each selected domain to extract:
     • Key skills/tools/frameworks expected
     • Industry use cases
     • Trending roles, platforms, orgs
     • Growth metrics, stability & relevance

4. **Gap Analysis**

   * Compare CV vs domain benchmarks
   * Categorize: ✅ matched, ⚠️ partial, ❌ missing

5. **Action Plan Creation**

   * Courses (with providers)
   * Certifications
   * Tools to learn
   * Project ideas
   * Experience-building steps (internships, gigs, open-source)

6. **Summarize and Present**

   * Clean sectioned markdown output
   * Metadata block for each insight
   * References for all external data

7. If the data is too large to be displayed at once, present the data in chunks untill you present the entire data

---

### 🧰 Tools & Agents

* `cv_agent` for resume extraction
* `google_domain_agent` (for focused domain intelligence)
* `google_search_tool` (general trend validation)
* `career_advisor_agent` for pathing
* `job_analysis_agent`, `news_opportunity_agent`

---

### ✅ Output Format

* If the data is too large to be displayed at once, present the data in chunks untill you present the entire data
```markdown
## ✅ Candidate Summary
{Concise overview from CV}

## 🔍 Domain Recommendations

### 🔹 Domain: [Domain Name]

**Why This Domain:**
- [Fit explanation: skills, experience, career interest]

**Typical Roles:** [ML Engineer, Data Analyst...]
**Salary Range:** $XXk–$YYk (USD)

#### 🔍 Gap Analysis
| Category       | Status     | Notes |
| --------       | ------     | ----- |
| Skills         | ⚠️ Partial | Python present, but no TensorFlow |
| Tools          | ✅         | Power BI, Tableau |
| Certifications | ❌ Missing | Suggest Google DA cert |
| Projects       | ⚠️         | Needs real-world datasets |

#### 🧠 Action Plan
- [Step 1: Learn X (High Priority)]
- [Step 2: Build project Y on GitHub]
- [Step 3: Earn Z certification]

#### 📚 Suggested Resources
| Area | Resources |
|------|-----------|
| ML | Coursera – Andrew Ng |
| Portfolio | GitHub, Kaggle |

#### 📌 Metadata
- Data Sources: [NVIDIA Careers](https://nvidia.com/careers), [McKinsey Future of Work](https://mckinsey.com/future-work)
- Retrieved via: `google_domain_agent`
- Scraped On: 2025-06-22
- Language: English
- Tags: AI, Robotics, Remote, Entry-level

---
```

### 📊 Output Blocks

* **response**: Direct suggestions and conversation with user
* **analytics**: Commentary, future outlook, strategic advice
* **data**: Structured tables and summaries
* **comments**: Optional internal or dev notes


    ''',
    tools=[AgentTool(googlesearch), AgentTool(googledomain)],
    #output_schema= domainschema,
    output_key="domaindata",
)
