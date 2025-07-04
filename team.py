
from agno.agent import Agent
from agno.models.google import Gemini
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.models.gemini import GeminiTools
from agno.tools import tool
from typing import Dict, List, Optional
import json
import re
# --- ADDED: dotenv import and load ---
from dotenv import load_dotenv
import os
load_dotenv()
# --- END ADDED ---

# Custom tools for LinkedIn content creation and networking
@tool
def analyze_linkedin_profile(linkedin_url: str) -> Dict:
    """Analyze LinkedIn profile to understand user's background and networking potential."""
    # In real implementation, this would scrape LinkedIn profile data
    # For demo purposes, we'll simulate profile analysis
    
    profile_data = {
        "name": "User Name",
        "current_role": "Software Engineer",
        "company": "Tech Company",
        "industry": "Technology",
        "experience_years": 5,
        "skills": ["Python", "Machine Learning", "Data Science"],
        "education": "Computer Science",
        "connection_count": 500,
        "recent_activity": "Active in AI and tech discussions"
    }
    
    return profile_data

@tool
def identify_target_companies(industry: str, role: str, location: str = "Global") -> List[Dict]:
    """Identify target companies for networking based on user's profile and goals."""
    
    # Sample target companies (in real implementation, use company databases/APIs)
    target_companies = [
        {
            "name": "Google",
            "industry": "Technology",
            "size": "Large",
            "networking_potential": "High",
            "key_people": ["Software Engineers", "Product Managers", "Data Scientists"],
            "content_strategy": "Share technical insights, open-source contributions, innovation thoughts"
        },
        {
            "name": "Microsoft",
            "industry": "Technology", 
            "size": "Large",
            "networking_potential": "High",
            "key_people": ["Cloud Engineers", "AI Researchers", "Developer Advocates"],
            "content_strategy": "Discuss cloud technologies, AI developments, developer tools"
        },
        {
            "name": "Startup Tech Companies",
            "industry": "Technology",
            "size": "Small-Medium",
            "networking_potential": "Medium",
            "key_people": ["Founders", "Early Engineers", "Growth Teams"],
            "content_strategy": "Share startup insights, growth hacking, innovation stories"
        }
    ]
    
    return target_companies

@tool
def generate_networking_hashtags(target_companies: List[str], industry: str) -> List[str]:
    """Generate hashtags specifically for networking with target company employees."""
    
    networking_hashtags = []
    
    # Company-specific hashtags
    for company in target_companies:
        company_clean = company.replace(" ", "").replace(",", "")
        networking_hashtags.extend([
            f"#{company_clean}",
            f"#{company_clean}Careers",
            f"#{company_clean}Tech"
        ])
    
    # Industry networking hashtags
    industry_hashtags = {
        "technology": ["#TechNetworking", "#SoftwareEngineers", "#TechCommunity", "#DevCommunity"],
        "ai": ["#AIEngineers", "#MachineLearning", "#DataScience", "#AIResearch"],
        "finance": ["#FinTech", "#Finance", "#Banking", "#FinanceJobs"],
        "healthcare": ["#HealthTech", "#Healthcare", "#MedTech", "#HealthcareIT"]
    }
    
    networking_hashtags.extend(industry_hashtags.get(industry.lower(), ["#Professional", "#Networking"]))
    
    return list(set(networking_hashtags))[:8]  # Limit to 8 unique hashtags

@tool
def create_networking_cta(target_companies: List[str], content_type: str) -> str:
    """Create call-to-action specifically designed for networking with target company employees."""
    
    cta_templates = {
        "learning": f"🤝 Fellow engineers at {', '.join(target_companies[:2])}, what's your experience with this? Would love to connect and learn from your insights!",
        "achievement": f"🎉 Excited to connect with amazing professionals at {', '.join(target_companies[:2])} and similar companies. Let's build something great together!",
        "insight": f"💭 What do you think, {', '.join(target_companies[:2])} team? Would love to hear your perspectives and connect with like-minded professionals!",
        "question": f"❓ Calling all experts at {', '.join(target_companies[:2])} - your insights would be invaluable! Let's connect and discuss.",
        "general": f"🌟 Always excited to connect with talented professionals at {', '.join(target_companies[:2])} and beyond. Let's grow our network together!"
    }
    
    return cta_templates.get(content_type, cta_templates["general"])

# Agent 1: Insight Generator Agent
insight_generator = Agent(
    name="Insight Generator",
    role="Transforms raw inputs into meaningful content insights for networking",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[DuckDuckGoTools(), analyze_linkedin_profile, identify_target_companies],
    description="Expert trend miner and networking strategist who transforms user inputs into engaging content insights that attract target company professionals.",
    instructions=[
        "You are a LinkedIn networking and content insight specialist.",
        "Your goal is to help users create content that attracts professionals from their target companies.",
        "When analyzing user inputs:",
        "1. Extract key insights that would interest professionals at target companies",
        "2. Research current trends relevant to the user's industry and target companies",
        "3. Identify networking opportunities and conversation starters",
        "4. Find common interests between user and target company employees",
        "5. Suggest content angles that showcase expertise while inviting collaboration",
        "",
        "Example Analysis Process:",
        "- User shares: 'Just learned about microservices architecture'",
        "- Research: Current microservices trends at Google, Microsoft, Netflix",
        "- Insight: 'Microservices adoption challenges and solutions that resonate with engineers at these companies'",
        "- Networking angle: 'Share learning journey + ask for experiences from senior engineers'",
        "",
        "Always focus on creating genuine value for target company professionals while positioning the user as someone worth connecting with."
    ],
    add_datetime_to_instructions=True,
    show_tool_calls=True
)

# Agent 2: Content Architect Agent  
content_architect = Agent(
    name="Content Architect",
    role="Designs networking-focused LinkedIn content with personal brand consistency",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[generate_networking_hashtags, create_networking_cta],
    description="LinkedIn content architect specializing in networking-focused posts that attract target company professionals while maintaining authentic personal brand.",
    instructions=[
        "You are a LinkedIn content architect focused on professional networking and relationship building.",
        "Your mission is to create content that naturally attracts professionals from target companies.",
        "",
        "Content Structure Guidelines:",
        "1. HOOK (First 2 lines): Grab attention of target company professionals",
        "2. STORY/INSIGHT: Share valuable experience or learning",
        "3. VALUE: Provide actionable insights or thought-provoking questions", 
        "4. NETWORKING CTA: Invite connection and conversation",
        "5. HASHTAGS: Strategic mix of industry + company-specific tags",
        "",
        "Example Post Structure:",
        "🚀 Just implemented a solution that reduced API response time by 60%",
        "(Hook targeting engineers)",
        "",
        "Here's what I learned about database optimization...",
        "(Story with technical value)",
        "",
        "The key insight: [specific technical detail]",
        "(Actionable value for peers)",
        "",
        "Fellow engineers at Google, Microsoft - what's your approach to this challenge?",
        "(Networking CTA)",
        "",
        "#SoftwareEngineering #Google #Microsoft #DatabaseOptimization",
        "(Strategic hashtags)",
        "",
        "Tone Guidelines:",
        "- Professional but approachable",
        "- Confident but humble",
        "- Knowledgeable but curious",
        "- Authentic and genuine",
        "- Focused on mutual value creation"
    ],
    show_tool_calls=True
)

# Agent 3: Post Publisher & Visualizer Agent
post_publisher = Agent(
    name="Post Publisher & Visualizer",
    role="Creates visuals and optimizes posts for maximum networking impact",
    # --- CHANGED: Pass GOOGLE_API_KEY from environment ---
    model=Gemini(id="gemini-2.0-flash-exp", api_key=os.getenv("GOOGLE_API_KEY")),
    tools=[GeminiTools(api_key=os.getenv("GOOGLE_API_KEY"))],
    # --- END CHANGED ---
    description="Visual content creator and LinkedIn optimization specialist focused on maximizing networking potential and engagement with target company professionals.",
    instructions=[
        "You are a LinkedIn visual content creator and networking optimization specialist.",
        "Your goal is to create visuals and optimize posts for maximum networking impact.",
        "",
        "Visual Content Guidelines:",
        "1. Create professional, clean visuals that appeal to corporate professionals",
        "2. Use company brand colors when relevant (Google colors for Google-focused content)",
        "3. Include key statistics, quotes, or insights in visual format",
        "4. Design carousel posts for complex topics (step-by-step guides, comparisons)",
        "5. Create infographics that professionals would want to share with their teams",
        "",
        "Optimization Strategies:",
        "1. Post timing: Optimize for when target company employees are most active",
        "2. Engagement hooks: Questions that encourage comments from target professionals",
        "3. Shareability: Content that target company employees would share internally",
        "4. Discussion starters: Topics that naturally lead to professional conversations",
        "",
        "Example Visual Ideas:",
        "- 'Before/After' performance improvements",
        "- 'Lessons Learned' infographics",
        "- 'Tech Stack Comparison' charts",
        "- 'Career Journey' timeline visuals",
        "- 'Industry Insights' data visualizations",
        "",
        "Always ensure visuals are:",
        "- Professional and corporate-friendly",
        "- Easy to read on mobile devices",
        "- Branded consistently with user's personal brand",
        "- Optimized for LinkedIn's image dimensions"
    ],
    show_tool_calls=True
)

# LinkedIn Content Creator Team
linkedin_content_team = Team(
    name="LinkedIn Networking Content Team",
    mode="coordinate", 
    model=Gemini(id="gemini-2.0-flash-exp"),
    members=[insight_generator, content_architect, post_publisher],
    description="Specialized team creating LinkedIn content designed to attract and network with professionals from target companies.",
    instructions=[
        "You are coordinating a team of LinkedIn networking specialists.",
        "Your mission: Transform user inputs into compelling content that attracts target company professionals.",
        "",
        "Workflow Process:",
        "1. INSIGHT GENERATOR: Analyze user input + research target companies + identify networking opportunities",
        "2. CONTENT ARCHITECT: Structure content for networking impact + create engaging copy + add strategic CTAs",
        "3. POST PUBLISHER: Create supporting visuals + optimize for engagement + provide posting strategy",
        "",
        "Success Criteria:",
        "- Content showcases user's expertise authentically",
        "- Naturally attracts target company professionals",
        "- Encourages meaningful professional conversations",
        "- Builds user's reputation as a valuable connection",
        "- Increases networking opportunities with target companies",
        "",
        "Always ensure the final content is:",
        "✅ Professional and corporate-appropriate",
        "✅ Valuable to target company employees", 
        "✅ Authentic to user's voice and experience",
        "✅ Optimized for LinkedIn's algorithm",
        "✅ Designed to generate meaningful connections"
    ],
    add_datetime_to_instructions=True,
    enable_agentic_context=True,
    share_member_interactions=True,
    show_members_responses=True,
    markdown=True,
    success_criteria="Create networking-focused LinkedIn content that attracts target company professionals, showcases user expertise, and generates meaningful professional connections and opportunities."
)

# Dynamic User Input Handler
class LinkedInContentCreator:
    def __init__(self):
        self.team = linkedin_content_team
        self.user_profile = {}
        self.target_companies = []
    
    def get_user_input(self):
        """Collect dynamic user input for content creation."""
        print("🚀 LinkedIn Networking Content Creator")
        print("=" * 50)
        
        # Basic user information
        self.user_profile = {
            "name": input("👤 Your Name: "),
            "linkedin_url": input("🔗 Your LinkedIn URL: "),
            "current_role": input("💼 Current Role: "),
            "company": input("🏢 Current Company: "),
            "industry": input("🏭 Industry: "),
            "experience_years": input("📅 Years of Experience: ")
        }
        
        # Target companies
        print("\n🎯 Target Companies for Networking:")
        target_input = input("Enter target companies (comma-separated): ")
        self.target_companies = [company.strip() for company in target_input.split(",")]
        
        # Content input
        print("\n📝 Content Information:")
        content_type = input("Content Type (learning/achievement/insight/question): ")
        content_details = input("Content Details: ")
        
        # Networking goals
        networking_goal = input("🤝 Networking Goal: ")
        
        return {
            "user_profile": self.user_profile,
            "target_companies": self.target_companies,
            "content_type": content_type,
            "content_details": content_details,
            "networking_goal": networking_goal
        }
    
    def create_networking_content(self, user_input: Dict):
        """Create LinkedIn content optimized for networking with target companies."""
        
        prompt = f"""
        Create a LinkedIn post optimized for networking with target company professionals:
        
        USER PROFILE:
        - Name: {user_input['user_profile']['name']}
        - Role: {user_input['user_profile']['current_role']}
        - Company: {user_input['user_profile']['company']}
        - Industry: {user_input['user_profile']['industry']}
        - Experience: {user_input['user_profile']['experience_years']} years
        
        TARGET COMPANIES: {', '.join(user_input['target_companies'])}
        
        CONTENT TYPE: {user_input['content_type']}
        CONTENT DETAILS: {user_input['content_details']}
        NETWORKING GOAL: {user_input['networking_goal']}
        
        REQUIREMENTS:
        1. Create content that naturally attracts professionals from target companies
        2. Include networking-focused call-to-action
        3. Use strategic hashtags including company-specific ones
        4. Showcase expertise while inviting collaboration
        5. Generate supporting visual if beneficial
        6. Provide posting strategy and timing recommendations
        
        The content should feel authentic and valuable, not salesy or desperate for connections.
        """
        
        return self.team.run(prompt)

# Example Usage and Demonstrations
def run_examples():
    """Run example scenarios to demonstrate the system."""
    
    print("🎯 LinkedIn Networking Content Creator - Examples")
    print("=" * 60)
    
    # Example 1: Learning Post for Google/Microsoft targeting
    example1 = {
        "user_profile": {
            "name": "Alex Chen",
            "current_role": "Senior Software Engineer", 
            "company": "TechStartup Inc",
            "industry": "Technology",
            "experience_years": "6"
        },
        "target_companies": ["Google", "Microsoft", "Meta"],
        "content_type": "learning",
        "content_details": "Just completed advanced Kubernetes certification and implemented a microservices architecture that improved our system scalability by 300%",
        "networking_goal": "Connect with senior engineers and architects at FAANG companies to discuss best practices and potential opportunities"
    }
    
    print("\n📚 EXAMPLE 1: Learning Achievement Post")
    print("-" * 40)
    creator = LinkedInContentCreator()
    result1 = creator.create_networking_content(example1)
    print(result1)

    # Add this at the end of your file to run the examples
if __name__ == "__main__":
    # You can either run examples or use the interactive mode
    choice = input("Run examples (e) or interactive mode (i)? ").lower()
    
    if choice == 'e':
        run_examples()
    else:
        creator = LinkedInContentCreator()
        user_input = creator.get_user_input()
        result = creator.create_networking_content(user_input)
        print("\n" + "="*60)
        print("🎯 GENERATED LINKEDIN CONTENT")
        print("="*60)
        print(result)