from agno.agent import Agent
from agno.models.google import Gemini
from agno.team.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from typing import List, Dict, Any, Optional
import json
import re
from datetime import datetime
import requests
from urllib.parse import urlparse

# Enhanced LinkedIn-specific tools with A/B testing and analytics
class LinkedInResearchTools:
    """Advanced tools for LinkedIn trend research and content analysis"""
    
    def analyze_linkedin_profile(self, linkedin_url: str) -> Dict[str, Any]:
        """Analyze LinkedIn profile to understand user's brand and network"""
        # Extract username from LinkedIn URL
        try:
            username = linkedin_url.split('/in/')[-1].split('/')[0]
            return {
                "username": username,
                "profile_strength": "professional",
                "industry_focus": "extracted_from_profile",
                "network_size": "estimated_from_connections",
                "content_style": "analyzed_from_recent_posts",
                "engagement_rate": "calculated_from_interactions"
            }
        except:
            return {"error": "Invalid LinkedIn URL format"}
    
    def research_target_companies(self, companies: List[str], industry: str) -> Dict[str, Any]:
        """Research target companies for networking opportunities"""
        company_insights = {}
        for company in companies:
            company_insights[company] = {
                "company_culture": f"Research insights about {company} culture",
                "recent_news": f"Latest developments at {company}",
                "employee_content_trends": f"What {company} employees are posting about",
                "networking_opportunities": f"Events and discussions related to {company}",
                "key_topics": ["innovation", "growth", "company values", "industry trends"],
                "best_engagement_approach": f"How to engage with {company} employees professionally"
            }
        return company_insights
    
    def analyze_industry_trends(self, industry: str, target_companies: List[str]) -> Dict[str, Any]:
        """Analyze current industry trends for better networking content"""
        return {
            "trending_topics": [f"{industry} innovation", "industry challenges", "future trends"],
            "popular_hashtags": [f"#{industry.lower()}", "#innovation", "#networking", "#professional"],
            "content_gaps": f"Underexplored topics in {industry}",
            "networking_events": f"Upcoming {industry} events and conferences",
            "thought_leaders": f"Key influencers in {industry}",
            "company_specific_trends": {company: f"Trends specific to {company}" for company in target_companies}
        }

class ContentFormattingTools:
    """Enhanced tools for formatting and A/B testing LinkedIn content"""
    
    def create_networking_post_variants(self, content: str, target_audience: str) -> List[Dict[str, Any]]:
        """Create multiple post variants for A/B testing"""
        variants = []
        
        # Variant 1: Story-based approach
        variants.append({
            "variant_type": "story_based",
            "hook": "Here's something that happened to me recently...",
            "structure": "personal_story_with_lesson",
            "tone": "authentic_and_relatable",
            "cta": "Has anyone else experienced this? I'd love to hear your thoughts!",
            "networking_angle": "builds_personal_connection"
        })
        
        # Variant 2: Insight-driven approach
        variants.append({
            "variant_type": "insight_driven",
            "hook": "I've been thinking about this industry trend...",
            "structure": "insight_analysis_with_implications",
            "tone": "thought_leadership",
            "cta": "What's your take on this? Especially curious about perspectives from [target_companies]",
            "networking_angle": "demonstrates_expertise"
        })
        
        # Variant 3: Question-based approach
        variants.append({
            "variant_type": "question_based",
            "hook": "Quick question for my network...",
            "structure": "question_context_discussion",
            "tone": "collaborative_and_curious",
            "cta": "Drop your thoughts below - always learning from this amazing community!",
            "networking_angle": "encourages_dialogue"
        })
        
        return variants
    
    def format_for_target_companies(self, content: str, target_companies: List[str], industry: str) -> str:
        """Format content to appeal to specific target companies"""
        formatted_content = content
        
        # Add company-specific context
        if target_companies:
            company_mention = f"Especially relevant for professionals at {', '.join(target_companies[:3])}"
            formatted_content += f"\n\n{company_mention}"
        
        # Add industry-specific hashtags
        industry_hashtags = {
            "tech": ["#TechCareers", "#Innovation", "#SoftwareDevelopment", "#AI", "#DigitalTransformation"],
            "finance": ["#FinTech", "#Banking", "#Investment", "#Finance", "#WealthManagement"],
            "healthcare": ["#HealthTech", "#MedicalInnovation", "#Healthcare", "#PatientCare"],
            "marketing": ["#MarketingStrategy", "#DigitalMarketing", "#BrandBuilding", "#CustomerExperience"],
            "consulting": ["#Consulting", "#BusinessStrategy", "#ProblemSolving", "#ClientSuccess"]
        }
        
        relevant_hashtags = industry_hashtags.get(industry.lower(), ["#Professional", "#Career", "#Growth"])
        hashtag_string = " ".join(relevant_hashtags[:8])
        formatted_content += f"\n\n{hashtag_string}"
        
        return formatted_content
    
    def optimize_for_algorithm(self, content: str) -> Dict[str, Any]:
        """Optimize content for LinkedIn algorithm"""
        return {
            "optimal_length": "1300-1800 characters for maximum reach",
            "engagement_triggers": ["questions", "calls_to_action", "personal_stories"],
            "posting_recommendations": {
                "best_times": ["Tuesday-Thursday 9AM-10AM", "1PM-2PM"],
                "frequency": "3-4 posts per week for optimal visibility",
                "engagement_window": "First 60 minutes are crucial for algorithm boost"
            },
            "algorithm_factors": {
                "early_engagement": "Critical for visibility",
                "comment_responses": "Respond within 1-2 hours",
                "connection_interactions": "Engage with your network's content"
            }
        }

class NetworkingOptimizationTools:
    """Tools for optimizing networking and professional connections"""
    
    def generate_networking_strategies(self, target_companies: List[str], user_background: str) -> Dict[str, Any]:
        """Generate personalized networking strategies"""
        strategies = {}
        
        for company in target_companies:
            strategies[company] = {
                "content_approach": f"Share insights relevant to {company}'s industry challenges",
                "engagement_tactics": [
                    f"Comment thoughtfully on {company} employees' posts",
                    f"Share relevant articles that {company} professionals would find valuable",
                    f"Ask insightful questions about {company}'s recent developments"
                ],
                "conversation_starters": [
                    f"I noticed {company} is focusing on [recent initiative]. As someone with {user_background}, I'm curious about...",
                    f"The work {company} is doing in [specific area] is fascinating. I'd love to learn more about...",
                    f"Having worked in {user_background}, I'm interested in {company}'s approach to..."
                ],
                "value_propositions": [
                    f"Share experiences from {user_background} that could benefit {company}",
                    f"Offer insights on industry trends relevant to {company}",
                    f"Provide a fresh perspective on {company}'s challenges"
                ]
            }
        
        return strategies
    
    def create_follow_up_sequences(self, interaction_type: str) -> List[str]:
        """Create follow-up sequences for different types of interactions"""
        sequences = {
            "post_engagement": [
                "Day 1: Like and comment on their post",
                "Day 3: Share their post with thoughtful commentary",
                "Day 7: Send connection request with personalized message",
                "Day 14: Follow up with relevant article or insight"
            ],
            "connection_accepted": [
                "Day 1: Thank them for connecting",
                "Day 5: Share relevant content they might find interesting",
                "Day 14: Ask thoughtful question about their work",
                "Day 30: Propose virtual coffee or collaboration"
            ],
            "comment_interaction": [
                "Day 1: Continue the conversation in comments",
                "Day 2: Like their follow-up responses",
                "Day 5: Share related content they might enjoy",
                "Day 10: Send connection request mentioning the discussion"
            ]
        }
        
        return sequences.get(interaction_type, ["Generic follow-up sequence"])

# Initialize enhanced tools
linkedin_research = LinkedInResearchTools()
content_formatting = ContentFormattingTools()
networking_optimization = NetworkingOptimizationTools()

# Agent 1: Insight Generator Agent (Enhanced)
insight_generator = Agent(
    name="InsightGenerator",
    role="LinkedIn Content Strategist & Trend Analyst",
    model=Gemini("gemini-2.5-pro"),
    description=(
        "I am your LinkedIn content strategist who transforms your experiences into networking gold. "
        "I research trends, analyze your target companies, and extract insights that make you stand out "
        "to the right people in your industry."
    ),
    instructions=[
        "CORE MISSION: Transform user inputs into networking-focused content insights that attract target company professionals.",
        
        "STEP 1 - ANALYZE USER INPUT:",
        "• Extract key experiences, skills, and achievements from their content",
        "• Identify their industry, role, and career aspirations",
        "• Note their target companies and networking goals",
        "• Understand their current LinkedIn presence and style",
        
        "STEP 2 - RESEARCH & INTELLIGENCE:",
        "• Research current trends in their industry using web search",
        "• Analyze what's trending at their target companies",
        "• Identify content gaps they can fill with their unique perspective",
        "• Find networking opportunities and relevant conversations",
        
        "STEP 3 - INSIGHT EXTRACTION:",
        "• Transform their experiences into valuable professional insights",
        "• Connect their learnings to broader industry trends",
        "• Identify multiple content angles from single experiences",
        "• Focus on insights that demonstrate expertise and thought leadership",
        
        "EXAMPLES OF GREAT INSIGHTS:",
        "• 'How a failed project taught me the most important lesson about team leadership'",
        "• 'The surprising connection between customer feedback and product innovation'",
        "• 'Why the best career advice I got came from an unexpected source'",
        "• 'The industry trend everyone's talking about - but here's what they're missing'",
        
        "NETWORKING FOCUS:",
        "• Ensure insights appeal to professionals at target companies",
        "• Create content that invites meaningful professional discussions",
        "• Identify opportunities to showcase expertise relevant to target roles",
        "• Generate insights that position user as a valuable industry connection"
    ],
    tools=[DuckDuckGoTools()],
    add_datetime_to_instructions=True,
)

# Agent 2: Content Architect Agent (Enhanced)
content_architect = Agent(
    name="ContentArchitect",
    role="LinkedIn Post Designer & Brand Strategist",
    model=Gemini("gemini-2.5-pro"),
    description=(
        "I am your LinkedIn content architect who transforms insights into compelling posts that build "
        "your professional brand and attract meaningful connections. I create multiple post variants "
        "for different networking strategies."
    ),
    instructions=[
        "CORE MISSION: Transform insights into engaging LinkedIn posts that build professional relationships and demonstrate expertise.",
        
        "STEP 1 - CONTENT STRATEGY:",
        "• Create 3 different post variants for A/B testing",
        "• Match content style to user's professional brand",
        "• Ensure each post serves a specific networking purpose",
        "• Balance authenticity with professional appeal",
        
        "STEP 2 - POST STRUCTURE (Use these proven formats):",
        "FORMAT 1 - Story-Based Post:",
        "• Hook: 'Here's something that happened...' or 'Last week, I learned...'",
        "• Story: Brief, relatable professional experience",
        "• Insight: What this teaches about the industry/role",
        "• CTA: 'Has anyone else experienced this?'",
        
        "FORMAT 2 - Insight-Driven Post:",
        "• Hook: 'I've been thinking about...' or 'Here's an unpopular opinion...'",
        "• Analysis: Deep dive into industry trend or challenge",
        "• Implications: Why this matters for professionals",
        "• CTA: 'What's your take on this?'",
        
        "FORMAT 3 - Question-Based Post:",
        "• Hook: 'Quick question for my network...'",
        "• Context: Brief background on the topic",
        "• Question: Specific, thought-provoking question",
        "• CTA: 'Drop your thoughts below!'",
        
        "STEP 3 - BRAND CONSISTENCY:",
        "• Maintain user's authentic voice and tone",
        "• Use consistent formatting and emoji style",
        "• Ensure professional language appropriate for target audience",
        "• Add personality while maintaining credibility",
        
        "EXAMPLES OF GREAT HOOKS:",
        "• 'The biggest mistake I see talented professionals make:'",
        "• 'Here's what 5 years in [industry] taught me about [topic]:'",
        "• 'Unpopular opinion: [controversial but thoughtful take]'",
        "• 'I used to think [common belief], but then [experience] changed my mind'",
        
        "NETWORKING OPTIMIZATION:",
        "• Create posts that invite specific target company professionals to engage",
        "• Include subtle mentions of industry challenges relevant to target companies",
        "• Use language that demonstrates expertise without being overly promotional",
        "• End with CTAs that encourage meaningful professional discussions"
    ],
    tools=[Newspaper4kTools()],
    add_datetime_to_instructions=True,
)

# Agent 3: Post Publisher & Networking Strategist (Enhanced)
post_publisher = Agent(
    name="PostPublisher",
    role="LinkedIn Publishing Expert & Networking Strategist",
    model=Gemini("gemini-2.5-pro"),
    description=(
        "I am your LinkedIn publishing expert who finalizes posts for maximum engagement and networking impact. "
        "I optimize everything from hashtags to posting times, and create comprehensive networking strategies."
    ),
    instructions=[
        "CORE MISSION: Finalize posts for maximum professional networking impact and provide comprehensive publishing strategy.",
        
        "STEP 1 - POST OPTIMIZATION:",
        "• Format posts with perfect LinkedIn spacing and readability",
        "• Add strategic emojis that enhance without overwhelming",
        "• Ensure mobile-friendly formatting (60% of LinkedIn traffic is mobile)",
        "• Create clear visual hierarchy with line breaks and bullet points",
        
        "STEP 2 - HASHTAG STRATEGY:",
        "• Research and select 8-10 relevant hashtags maximum",
        "• Mix popular hashtags (1M+ posts) with niche ones (10K-100K posts)",
        "• Include industry-specific hashtags that target company professionals use",
        "• Add 2-3 hashtags specific to target companies or their focus areas",
        
        "STEP 3 - ENGAGEMENT OPTIMIZATION:",
        "• Recommend optimal posting times based on target audience",
        "• Suggest engagement tactics for first 60 minutes (critical for algorithm)",
        "• Create conversation starters that encourage meaningful comments",
        "• Provide follow-up comment responses to maintain engagement",
        
        "STEP 4 - NETWORKING STRATEGY:",
        "• Identify specific professionals likely to engage with this content",
        "• Create personalized outreach messages for high-value connections",
        "• Suggest follow-up actions after post publication",
        "• Provide templates for responding to comments and new connections",
        
        "POST FORMATTING STANDARDS:",
        "• First sentence: Strong hook (under 125 characters for mobile preview)",
        "• Body: 3-5 short paragraphs with single line breaks between",
        "• Key points: Use bullet points or numbered lists for clarity",
        "• CTA: Clear, specific call-to-action that encourages engagement",
        "• Hashtags: Separate line at bottom, grouped by relevance",
        
        "ENGAGEMENT TACTICS:",
        "• Tag relevant people (sparingly - max 2-3 per post)",
        "• Ask specific questions that require thoughtful responses",
        "• Share personal experiences that others can relate to",
        "• Use 'agree/disagree' frameworks to encourage discussion",
        
        "NETWORKING FOLLOW-UP:",
        "• Provide 48-hour engagement plan post-publication",
        "• Create personalized connection request templates",
        "• Suggest relevant content to share with new connections",
        "• Outline strategy for building relationships beyond the initial post"
    ],
    add_datetime_to_instructions=True,
)

# Enhanced LinkedIn Content Creator Team
linkedin_content_team = Team(
    name="LinkedInContentTeam",
    mode="coordinate",
    model=Gemini("gemini-2.5-pro"),
    members=[insight_generator, content_architect, post_publisher],
    description=(
        "We are your LinkedIn content creation and networking team. We transform your professional "
        "experiences into engaging content that builds your brand and attracts meaningful connections "
        "from your target companies. Every post is strategically designed to advance your networking goals."
    ),
    instructions=[
        "TEAM MISSION: Create LinkedIn content that builds professional relationships and advances career goals through strategic networking.",
        
        "WORKFLOW COORDINATION:",
        "1. INSIGHT GENERATOR analyzes user input and researches networking opportunities",
        "2. CONTENT ARCHITECT creates multiple post variants optimized for different networking strategies",
        "3. POST PUBLISHER finalizes content and provides comprehensive networking strategy",
        
        "TEAM STANDARDS:",
        "• Every post must serve a clear networking purpose",
        "• All content should demonstrate expertise and thought leadership",
        "• Focus on building genuine professional relationships, not just followers",
        "• Provide actionable strategies beyond just content creation",
        
        "OUTPUT REQUIREMENTS:",
        "• 3 post variants with different networking approaches",
        "• Complete formatting ready for LinkedIn publication",
        "• Hashtag strategy with reasoning",
        "• Posting time and engagement recommendations",
        "• Follow-up networking strategy",
        "• Templates for connection requests and responses",
        
        "QUALITY CONTROL:",
        "• Ensure authenticity - content should sound like the user",
        "• Maintain professional standards appropriate for target companies",
        "• Verify all claims and avoid overstatements",
        "• Check for potential misunderstandings or controversial elements",
        
        "SUCCESS METRICS:",
        "• Content attracts engagement from target company professionals",
        "• Posts generate meaningful professional discussions",
        "• User receives relevant connection requests",
        "• Content positions user as knowledgeable industry professional"
    ],
    add_datetime_to_instructions=True,
    add_member_tools_to_system_message=False,
    enable_agentic_context=True,
    share_member_interactions=True,
    show_members_responses=True,
    markdown=True,
)

# Enhanced User Input Handler
class UserInputHandler:
    """Handle dynamic user input and profile analysis"""
    
    def __init__(self):
        self.user_profile = {}
        self.content_history = []
    
    def collect_user_input(self) -> Dict[str, Any]:
        """Collect comprehensive user input for content creation"""
        print("🚀 LinkedIn Content Creator - Let's build your professional presence!")
        print("=" * 60)
        
        # Basic profile information
        print("\n📋 PROFILE SETUP:")
        linkedin_url = input("Your LinkedIn Profile URL: ").strip()
        industry = input("Your Industry (e.g., tech, finance, healthcare): ").strip()
        current_role = input("Your Current Role: ").strip()
        experience_level = input("Experience Level (entry/mid/senior/executive): ").strip()
        
        # Target companies and networking goals
        print("\n🎯 NETWORKING GOALS:")
        target_companies = input("Target Companies (comma-separated): ").strip().split(',')
        target_companies = [company.strip() for company in target_companies if company.strip()]
        
        networking_goals = input("Networking Goals (e.g., job opportunities, partnerships, learning): ").strip()
        
        # Content input
        print("\n📝 CONTENT INPUT:")
        print("What would you like to create content about?")
        print("Examples:")
        print("• Recent learning or certification")
        print("• Career milestone or achievement")
        print("• Industry insight or trend observation")
        print("• Project experience or lesson learned")
        print("• Professional challenge overcome")
        
        content_topic = input("\nYour content topic/experience: ").strip()
        
        # Additional context
        print("\n🔍 ADDITIONAL CONTEXT:")
        recent_posts = input("Paste a recent LinkedIn post of yours (to understand your style): ").strip()
        key_skills = input("Key skills you want to showcase: ").strip()
        career_goals = input("Career goals/aspirations: ").strip()
        
        # Compile user input
        user_input = {
            "profile": {
                "linkedin_url": linkedin_url,
                "industry": industry,
                "current_role": current_role,
                "experience_level": experience_level,
                "key_skills": key_skills,
                "career_goals": career_goals
            },
            "networking": {
                "target_companies": target_companies,
                "networking_goals": networking_goals
            },
            "content": {
                "topic": content_topic,
                "recent_posts": recent_posts,
                "style_preference": "professional_with_personality"
            },
            "timestamp": datetime.now().isoformat()
        }
        
        return user_input
    
    def format_for_team(self, user_input: Dict[str, Any]) -> str:
        """Format user input for the LinkedIn team"""
        return f"""
        🎯 LINKEDIN CONTENT CREATION REQUEST
        
        👤 USER PROFILE:
        • LinkedIn: {user_input['profile']['linkedin_url']}
        • Industry: {user_input['profile']['industry']}
        • Role: {user_input['profile']['current_role']}
        • Experience: {user_input['profile']['experience_level']}
        • Key Skills: {user_input['profile']['key_skills']}
        • Career Goals: {user_input['profile']['career_goals']}
        
        🎯 NETWORKING GOALS:
        • Target Companies: {', '.join(user_input['networking']['target_companies'])}
        • Networking Objectives: {user_input['networking']['networking_goals']}
        
        📝 CONTENT REQUEST:
        Topic/Experience: {user_input['content']['topic']}
        
        Recent Post Example (for style reference):
        {user_input['content']['recent_posts'][:200]}...
        
        🚀 DELIVERABLES NEEDED:
        1. Create 3 post variants (story-based, insight-driven, question-based)
        2. Optimize for networking with target companies
        3. Include comprehensive hashtag strategy
        4. Provide posting and engagement recommendations
        5. Create follow-up networking strategy
        
        Focus on creating content that attracts meaningful professional connections and showcases expertise relevant to the target companies.
        """

# Example usage and testing
def main():
    """Main function to demonstrate the LinkedIn Content Creator Team"""
    
    # Initialize input handler
    input_handler = UserInputHandler()
    
    # Option 1: Interactive input
    print("Choose input method:")
    print("1. Interactive input (recommended)")
    print("2. Use example data")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        user_input = input_handler.collect_user_input()
    else:
        # Example data for testing
        user_input = {
            "profile": {
                "linkedin_url": "https://linkedin.com/in/johnsmith",
                "industry": "tech",
                "current_role": "Software Engineer",
                "experience_level": "mid",
                "key_skills": "Python, AI/ML, Cloud Computing",
                "career_goals": "Senior Engineer at top tech company"
            },
            "networking": {
                "target_companies": ["Google", "Microsoft", "Amazon"],
                "networking_goals": "Connect with senior engineers and hiring managers"
            },
            "content": {
                "topic": "Just completed AWS certification and built a serverless application that reduced processing time by 60%",
                "recent_posts": "Usually share technical insights with a conversational tone, use relevant emojis",
                "style_preference": "professional_with_personality"
            },
            "timestamp": datetime.now().isoformat()
        }
    
    # Format input for team
    formatted_input = input_handler.format_for_team(user_input)
    
    # Generate content
    print("\n" + "="*60)
    print("🚀 PROCESSING YOUR LINKEDIN CONTENT...")
    print("="*60)
    
    # Create LinkedIn content using the team
    response = linkedin_content_team.print_response(formatted_input)
    
    print("\n" + "="*60)
    print("✅ LINKEDIN CONTENT READY!")
    print("="*60)
    print("Your professional posts are optimized for networking success!")
    print("Follow the provided strategy to maximize your networking impact.")

if __name__ == "__main__":
    main()