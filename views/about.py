import streamlit as st

st.image(r"E:\Streamlit\assets\logo.png")

@st.dialog("Contact Me")
def show_contact_form():
    st.write("Email 📧 : sahilpohekar04@gmail.com")
    st.write("Phone 📞 : +91-9673630934")
    st.write("linkedin 🔗: https://www.linkedin.com/in/sahil-pohekar/")


# Title of the app
st.title("DeepSeek-R1: The $6 Million Underdog Challenging OpenAI’s AI Crown")

# Introduction
st.header("How a Chinese Startup’s Side Project Rewrote the Rules of AI Economics")

# Part 1: The “Thinking” AI Revolution
st.subheader("Part 1: The “Thinking” AI Revolution")
st.write("""
Imagine asking an AI not just to write a poem, but to explain its metaphors. Or to solve a physics problem by showing its work like a gifted student. That’s the promise of reasoning models—AI that thinks, not just calculates.
""")

# Traditional AI vs. Reasoning Models
st.write("**Traditional AI vs. Reasoning Models**")
st.write("""
| Standard AI (ChatGPT) | Reasoning AI (DeepSeek-R1) |
|-----------------------|----------------------------|
| Pattern-matching      | Step-by-step logic         |
| “Best guess” answers  | Transparent reasoning trails|
| Struggles with new scenarios | Adapts like a human expert |
""")

st.write("""
*Example*: Ask GPT-4 to solve “If John has 5 apples and eats 2, how many remain?” It answers “3.” But ask why, and it stumbles. DeepSeek-R1 would break it down:
1. Start with 5 apples.
2. Subtract 2 eaten.
3. 5 - 2 = 3.

This “chain-of-thought” approach is why Silicon Valley is sweating over DeepSeek’s latest move.
""")

# Part 2: Meet the Giant-Slayer – DeepSeek-R1
st.subheader("Part 2: Meet the Giant-Slayer – DeepSeek-R1")
st.write("**The $6 Million Model That Outsmarts Billion-Dollar Tech**")

# 3 Reasons R1 Shook the AI World
st.write("**3 Reasons R1 Shook the AI World**")
st.write("""
1. **Price Tag Shock**
   - Trains for **$6 million** (vs. GPT-4’s rumored $100M+)
   - Operates at 1/50th the cost of OpenAI models
   - **How?** Secret sauce: Dynamic token selection – it ignores redundant data like a chef skimming a recipe.

2. **Multilingual Maverick**
   - While Western models fumble with Chinese idioms, R1 aces:
     - Classical poetry analysis
     - Technical jargon translation
     - Legal document parsing

3. **Built by Wall Street Refugees**
   - The twist? R1’s creators are quant traders from High-Flyer, a hedge fund.
   - Their edge:
     - Algorithmic frugality (trading taught them to optimize every byte)
     - Existing 10,000 Nvidia A100 chips repurposed for AI

*Fun Fact*: R1 began as a side project while the team focused on stock-picking algorithms!
""")

# Part 3: The Dark Side of Disruption
st.subheader("Part 3: The Dark Side of Disruption")
st.write("**Where DeepSeek-R1 Stumbles – And Why It Matters**")

# The 4 Achilles’ Heels
st.write("**The 4 Achilles’ Heels**")
st.write("""
1. **Mid-Answer Freezes**
   - Users report R1 sometimes stops dead during complex reasoning – like a GPS losing signal mid-route.

2. **Fact or Fiction?**
   - While brilliant at logic, R1 occasionally:
     - Invents fake historical dates
     - Misquotes scientific studies
     - Struggles with niche topics (e.g., Basque poetry)

3. **The Great Firewall of AI**
   - To comply with China’s laws, R1:
     - Dodges questions on Tibet/Taiwan
     - Refuses to debate political systems
   - **Result**: Less “free speech” than Western models.

4. **The Nvidia Dilemma**
   - Despite claims of independence, R1 relies on Nvidia H800 chips – now banned for export to China.
   - Can it survive without them?
""")

# Part 4: Why This Changes Everything
st.subheader("Part 4: Why This Changes Everything")
st.write("**A Blueprint for the Future of AI – Or a Fluke?**")

# The Big Picture
st.write("**The Big Picture**")
st.write("""
- **For Startups**: Proof you don’t need Big Tech’s billions to innovate.
- **For China**: A geopolitical win in the AI arms race.
- **For You**: Cheaper, faster AI tools could soon power everything from coding assistants to medical diagnostics.

**What’s Next?**
- Can DeepSeek fix R1’s “freezing” issue?
- Will the U.S. tighten chip controls further?
- Could quant-driven AI become a new trend?

**Final Verdict**
DeepSeek-R1 isn’t perfect – but it’s a warning shot to Silicon Valley. For the first time, a startup has matched GPT-4’s brains with a bootstrapper’s budget. Whether it’s the future of AI or a flash in the pan, one thing’s clear: The age of AI monopolies is over.
""")




st.markdown("---")

# Interactive Hooks
st.markdown("<h3>What do you think? Will reasoning models like R1 dominate? Share your thoughts below!</h3>", unsafe_allow_html=True)


if st.button("📧 Contact Me"):
    show_contact_form()
   






