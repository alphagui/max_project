import streamlit as st
from max import find_max_value

st.title("数学表达式最大值计算器")

st.write("请输入5个数字，用空格分隔：")
numbers_input = st.text_input("数字", "")

if st.button("计算最大值"):
    try:
        numbers = list(map(int, numbers_input.split()))
        if len(numbers) != 5:
            st.error("请输入正好5个数字。")
        else:
            max_value, max_expression = find_max_value(numbers)

            if max_value > 0:
                st.success(f"最大值 (小于等于100): {max_value}")
                st.info(f"表达式: {max_expression}")
            else:
                st.warning("没有找到结果在0到100之间的有效表达式。")
    except ValueError:
        st.error("请输入有效的数字，并用空格分隔。")