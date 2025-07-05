import streamlit as st

def show():
    if "expression" not in st.session_state:
        st.session_state.expression = ""

    if "numlock" not in st.session_state:
        st.session_state.numlock = True

    if "result" not in st.session_state:
        st.session_state.result = ""

    if "history" not in st.session_state:
        st.session_state.history = []

    

    # Set page configuration
    st.set_page_config(page_title="Calculator", page_icon="🧮", layout="wide")



    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        with st.container():
            with st.expander("📜 View Calculation History", expanded=True):
                if st.session_state.history:
                    for item in reversed(st.session_state.history[-2:]):
                        st.markdown(f"- `{item}`")
                else:
                    pass

    with col2:
        with st.container():
            st.markdown("<h1 style='text-align: left;'>🧮 Basic Calculator</h1>", unsafe_allow_html=True)
            st.header("Developed by Danyal Shafqat")
            col_input, col_button = st.columns([5, 1])
            

            with col_input:
                st.text_input("🔢 Start typing numbers...", 
                    value=st.session_state.expression, 
                    key="display",  )
                st.markdown("""
        <style>
        input[type="text"] {
            padding-top: 12px !important;
            padding-bottom: 12px !important;
            height: auto !important;
            font-size: 1.2rem !important;
            border-radius: 10px !important;
            border: 2px solid #4CAF50 !important;
            background-color: #f0f0f0 !important;
            color: #333 !important;
            width: 100% !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
            transition: all 0.2s ease-in-out !important;
            text-align: right !important;
            font-weight: bold !important;
            font-family: 'Courier New', Courier, monospace !important;
            caret-color: #4CAF50 !important;
            outline: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

            with col_button:
                st.markdown("""
        <style>
        .stButton > button {
            height: 3.5rem;
            margin-bottom: 0px;
            margin-top: 0px;
        }
        </style>
    """, unsafe_allow_html=True)
                if st.button("🧹 Clear", key="clear_button"):
                    st.session_state.expression = ""
                    st.rerun()

    with col3:
        with st.container():
            pass

    left_space, button_col1, button_col2, button_col3, button_col4, right_space = st.columns([2, 1, 1, 1, 1, 2])

    with button_col3:
        if st.button("⌫ Backspace"):
            st.session_state.expression = st.session_state.expression[:-1]
            st.rerun()

    with button_col1:
        if st.button(f"🔐 NumLock ({'ON' if st.session_state.numlock else 'OFF'})"):
            st.session_state.numlock = not st.session_state.numlock
            st.rerun()

    with button_col2:
        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.rerun()

    with button_col4:
        if st.button("="):
            expression = st.session_state.expression
            try:
                result = eval(expression, {"__builtins__": None}, {})
                st.session_state.expression = str(result)
                entry = f"{expression} = {result} ✅"
                st.session_state.history.append(entry)
            except ZeroDivisionError:
                st.session_state.expression = "Cannot divide by zero ❌"
                st.session_state.history.append(f"{expression} = ❌ Division Error")
            except Exception:
                st.session_state.expression = "Error ❌"
                st.session_state.history.append(f"{expression} = ❌ Error")
            st.rerun()

    left_space, col1, col2, col3, col4, right_space = st.columns([2, 1, 1, 1, 1, 2])

    st.markdown(
        """
        <style>
        .stButton > button {
            width: 100%;
            height: 3.5rem;
            font-size: 2rem; important;
            font-weight: extra bold; important;
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            border: none;
            margin-bottom: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #4CAF50;
            color: white !important;
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
            transform: scale(1.02);
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with col1:
        st.button("9", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "9"
        ), disabled=not st.session_state.numlock)

    with col2:
        st.button("8", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "8"
        ), disabled=not st.session_state.numlock)

    with col3:
        st.button("7", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "7"
        ), disabled=not st.session_state.numlock)

    with col4:
        if st.button("✖️ Multiply", key="multiply"):
            st.session_state["expression"] = st.session_state.get("expression", "") + "*"
            st.rerun()

    with col1:
        st.button("6", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "6"
        ), disabled=not st.session_state.numlock)

    with col2:
        st.button("5", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "5"
        ), disabled=not st.session_state.numlock)

    with col3:
        st.button("4", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "4"
        ), disabled=not st.session_state.numlock)

    with col4:
        if st.button("➗ Divide", key="divide"):
            st.session_state["expression"] = st.session_state.get("expression", "") + "/"
            st.rerun()

    with col1:
        st.button("3", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "3"
        ), disabled=not st.session_state.numlock)

    with col2:
        st.button("2", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "2"
        ), disabled=not st.session_state.numlock)

    with col3:
        st.button("1", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "1"
        ), disabled=not st.session_state.numlock)

    with col4:
        if st.button("➖ Subtract", key="subtract"):
            st.session_state["expression"] = st.session_state.get("expression", "") + "-"
            st.rerun()

    with col1:
        st.button("0", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "0"
        ), disabled=not st.session_state.numlock)

    with col2:
        st.button("00", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "00"
        ), disabled=not st.session_state.numlock)

    with col3:
        st.button(".", on_click=lambda: st.session_state.update(
            expression=st.session_state.expression + "."
        ), disabled=not st.session_state.numlock)

    with col4:
        if st.button("➕ Add", key="add"):
            st.session_state["expression"] = st.session_state.get("expression", "") + "+"
            st.rerun()

    st.write("---")
show()