import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#######################################
# Define callback functions for labs
#######################################
def reset_parameters():
    st.session_state["vix_level_slider"] = 20.0
    st.session_state["market_return_slider"] = 0.08
    st.session_state["volatility_impact_slider"] = 1.0

def set_lab1_parameters():
    st.session_state["vix_level_slider"] = 30.0
    st.session_state["market_return_slider"] = -0.05
    st.session_state["volatility_impact_slider"] = 1.5

def set_lab2_parameters():
    st.session_state["vix_level_slider"] = 15.0
    st.session_state["market_return_slider"] = 0.10
    st.session_state["volatility_impact_slider"] = 0.8

def set_lab3_parameters():
    st.session_state["vix_level_slider"] = 40.0
    st.session_state["market_return_slider"] = -0.10
    st.session_state["volatility_impact_slider"] = 2.0

#######################################
# Helper function to simulate VIX impact
#######################################
def calculate_vix_impact(vix_level, market_return, volatility_impact):
    # Simulate how VIX impacts market sentiment and returns
    adjusted_return = market_return - (vix_level / 100) * volatility_impact
    return adjusted_return

#######################################
# Configure the Streamlit app
#######################################
st.set_page_config(layout="wide")
st.title("📊 Understanding the VIX Index: The Fear Gauge")
st.markdown("""
The **VIX Index** measures market expectations of near-term volatility based on S&P 500 options. It is often called the "fear gauge" because it spikes during periods of market uncertainty.  
$$
\text{VIX} \propto \sigma_{\text{implied}}
$$
Where:
- $ \sigma_{\text{implied}} $: Implied volatility derived from option prices.
- High VIX: Indicates high expected volatility (uncertainty).
- Low VIX: Indicates low expected volatility (calm markets).
""")

# Sidebar for input parameters
with st.sidebar:
    st.header("⚙️ Parameters")
    
    # Reset button
    st.button("↺ Reset Parameters", on_click=reset_parameters)
    
    vix_level = st.slider("VIX Level", 10.0, 50.0, 20.0, key="vix_level_slider")
    market_return = st.slider("Market Return ($E(R_m)$)", -0.1, 0.2, 0.08, key="market_return_slider")
    volatility_impact = st.slider("Volatility Impact Factor", 0.5, 2.0, 1.0, key="volatility_impact_slider")
    
    # Disclaimer and license
    st.markdown("---")
    st.markdown(
        """
        **⚠️ Important Legal Disclaimer**  
        This tool is purely for educational purposes. No accuracy guarantees are provided.  
        The author does not engage in financial advising or endorse any specific investment strategies.  
        All information provided is for illustrative and educational purposes only.  

        **License:**  
        This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).  
        ![License Badge](https://licensebuttons.net/l/by-nc/4.0/88x31.png)  
        By Luís Simões da Cunha  
        """,
        unsafe_allow_html=True
    )

# Create tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs([
    "🎮 Interactive Tool", 
    "📚 Theory Behind VIX", 
    "📖 Comprehensive Tutorial", 
    "🛠️ Practical Labs"
])

# Tab 1: Interactive Tool
with tab1:
    # Calculate VIX impact
    adjusted_return = calculate_vix_impact(vix_level, market_return, volatility_impact)
    
    # Display results in columns
    col1, col2 = st.columns([1, 3])
    with col1:
        st.success(f"### Adjusted Market Return: **{adjusted_return:.2%}**")
        st.markdown(f"""
        ### Key Parameters
        - **VIX Level:** `{vix_level:.1f}`
        - **Market Return ($E(R_m)$):** `{market_return:.2%}`
        - **Volatility Impact Factor:** `{volatility_impact:.2f}`
        """)
    
    with col2:
        # Visualize VIX impact
        fig, ax = plt.subplots(figsize=(10, 5))
        vix_levels = np.linspace(10, 50, 100)
        adjusted_returns = market_return - (vix_levels / 100) * volatility_impact
        
        ax.plot(vix_levels, adjusted_returns, label="Adjusted Market Return", color="darkred", linewidth=2)
        ax.scatter(vix_level, adjusted_return, color="blue", label=f"Current VIX={vix_level:.1f}", zorder=5)
        ax.axhline(market_return, color="gray", linestyle="--", label="Original Market Return")
        ax.set_title("Impact of VIX on Market Returns", fontweight="bold")
        ax.set_xlabel("VIX Level")
        ax.set_ylabel("Adjusted Market Return")
        ax.grid(alpha=0.3)
        ax.legend()
        st.pyplot(fig)

# Tab 2: Theory Behind VIX
with tab2:
    st.markdown("""
    ## Volatility Index (VIX): Mathematical Foundation
    
    ### Overview
    The VIX measures implied volatility derived from S&P 500 index options. It reflects market expectations of 30-day forward-looking volatility.  
    Key points:
    - High VIX: Indicates fear or uncertainty in the market.
    - Low VIX: Indicates calm and stability.
    
    ### Core Equation

$$
\text{VIX} \approx \sqrt{\frac{2}{T} \sum_{i} \frac{\Delta K_i}{K_i^2} e^{rT} Q(K_i) - \frac{1}{T} \left( \frac{F}{K_0} - 1 \right)^2}
$$

Where:
- $ T $: Time to expiration.
- $ K_i $: Strike price of the $ i $-th option.
- $ Q(K_i) $: Midpoint of the bid-ask spread for each option.
- $ F $: Forward index level.
- $ r $: Risk-free rate.
    ### Key Insights
    - **Implied Volatility**: Reflects market sentiment about future price movements.
    - **Fear Gauge**: Spikes during market downturns or crises.
    - **Contrarian Indicator**: Extremely high VIX levels may signal oversold conditions.
    """)

# Tab 3: Comprehensive Tutorial
with tab3:
    st.markdown("""
    ## Welcome to the VIX Learning Tool!
    
    **What this tool does:**  
    This interactive calculator helps you understand how the VIX Index impacts market sentiment and expected returns. Perfect for learning about volatility and risk!
    
    ### Quick Start Guide
    
    1. **Adjust Parameters** (Left Sidebar):
       - Move sliders to set VIX level, market return, and volatility impact factor.
    
    2. **View Results** (Main Panel):
       - Real-time adjusted market return calculation.
       - Visualize the impact of VIX on market returns.
    
    3. **Try These Examples**:
       - 📉 Set VIX = 40: Notice how market returns drop due to high volatility.
       - 📈 Set VIX = 15: See how calm markets boost confidence.
       - 💹 Compare VIX = 20 vs VIX = 30: Observe sensitivity to volatility changes.
    
    **Pro Tip:** Use the reset button ↺ to quickly return to default values!
    """)

# Tab 4: Practical Labs
with tab4:
    st.header("🔬 Practical VIX Labs")
    st.markdown("""
    Welcome to the **Practical VIX Labs** section! Each lab provides a real-world scenario or demonstration 
    to help you apply the VIX concept in a hands-on way.
    
    Use the **"Set Lab Parameters"** buttons to jump directly to recommended settings for each scenario.
    Experiment, take notes, and enjoy exploring how volatility impacts markets!
    """)
    
    # --- Additional Disclaimer ---
    st.warning("""
    **Disclaimer**:  
    This material is purely for educational purposes. Do not use this tool for financial decisions without consulting a qualified professional.
    """)

    # A radio to choose one of the labs
    lab_choice = st.radio(
        "Select a lab to view:",
        ("Lab 1: Market Downturn",
         "Lab 2: Calm Markets",
         "Lab 3: Extreme Volatility"),
        index=0
    )
    
    # ---------------- Lab 1 ----------------
    if lab_choice == "Lab 1: Market Downturn":
        st.subheader("📉 Lab 1: Market Downturn and VIX Spike")
        st.markdown("""
        **Real-World Scenario:**  
        During a market crash, the VIX spikes as investors panic. How does this affect market returns?
        
        **Learning Objective:**  
        - Understand the relationship between VIX spikes and market sentiment.
        - Analyze the impact of high volatility on returns.
        
        **Suggested Steps**:
        1. Click "**Set Lab 1 Parameters**" to use VIX = 30, $E(R_m) = -5\\%$, Volatility Impact = 1.5.
        2. Observe the adjusted market return.
        3. Increase VIX to 40. Repeat the analysis.
        """)
        
        # Button to set Lab 1 parameters
        st.button("⚡ Set Lab 1 Parameters", on_click=set_lab1_parameters, key="lab1_setup")

    # ---------------- Lab 2 ----------------
    elif lab_choice == "Lab 2: Calm Markets":
        st.subheader("📈 Lab 2: Calm Markets and Low VIX")
        st.markdown("""
        **Real-World Scenario:**  
        In calm markets, the VIX remains low. How does this affect investor confidence and returns?
        
        **Learning Objective:**  
        - Explore the relationship between low VIX and positive market sentiment.
        - Understand why low volatility boosts returns.
        
        **Suggested Steps**:
        1. Click "**Set Lab 2 Parameters**" to use VIX = 15, $E(R_m) = 10\\%$, Volatility Impact = 0.8.
        2. Observe the adjusted market return.
        3. Decrease VIX to 10. Repeat the analysis.
        """)
        
        # Button to set Lab 2 parameters
        st.button("⚡ Set Lab 2 Parameters", on_click=set_lab2_parameters, key="lab2_setup")

    # ---------------- Lab 3 ----------------
    else:  # Lab 3: Extreme Volatility
        st.subheader("🔥 Lab 3: Extreme Volatility")
        st.markdown("""
        **Real-World Scenario:**  
        During extreme events (e.g., financial crises), the VIX can reach unprecedented levels. How does this impact markets?
        
        **Learning Objective:**  
        - Understand the role of extreme volatility in market crashes.
        - Analyze the potential for contrarian opportunities.
        
        **Suggested Steps**:
        1. Click "**Set Lab 3 Parameters**" to use VIX = 40, $E(R_m) = -10\\%$, Volatility Impact = 2.0.
        2. Observe the adjusted market return.
        3. Simulate recovery by reducing VIX to 20. Repeat the analysis.
        """)
        
        # Button to set Lab 3 parameters
        st.button("⚡ Set Lab 3 Parameters", on_click=set_lab3_parameters, key="lab3_setup")