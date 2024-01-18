import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon=":bar_chart:",
    )

    st.write("# ALX SE 2022 ANALYSIS")

    st.sidebar.success("Select a chart to visualise")

    st.markdown(
        """
      
    """
    )


if __name__ == "__main__":
    run()
