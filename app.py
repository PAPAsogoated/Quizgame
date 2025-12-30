import streamlit as st
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# ---------- SETUP ----------
st.title("🧠 Quiz App")

# Initialize session state (VERY IMPORTANT)
if "quiz" not in st.session_state:
    question_bank = []
    for q in question_data:
        question_bank.append(Question(q["text"], q["answer"]))
    st.session_state.quiz = QuizBrain(question_bank)
    st.session_state.feedback = ""
    st.session_state.finished = False

quiz = st.session_state.quiz

# ---------- PLAYER NAME ----------
if "player_name" not in st.session_state:
    st.session_state.player_name = st.text_input("Enter your name")

    if st.session_state.player_name:
        st.success(f"Welcome {st.session_state.player_name}!")
        st.rerun()

# ---------- QUIZ ----------
elif quiz.still_has_question() and not st.session_state.finished:
    q = quiz.current_question()

    st.subheader(f"Question {quiz.question_number + 1}")
    st.write(q.tx)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("True"):
            correct, answer = quiz.check_answer("True")
            st.session_state.feedback = (
                "✅ Correct!" if correct else f"❌ Wrong! Correct answer: {answer}"
            )
            st.rerun()

    with col2:
        if st.button("False"):
            correct, answer = quiz.check_answer("False")
            st.session_state.feedback = (
                "✅ Correct!" if correct else f"❌ Wrong! Correct answer: {answer}"
            )
            st.rerun()

    st.info(st.session_state.feedback)
    st.write(f"Score: {quiz.current_score}/{quiz.question_number}")

# ---------- RESULTS ----------
else:
    st.session_state.finished = True
    st.subheader("🎉 Quiz Completed!")

    total = quiz.question_number
    score = quiz.current_score
    percentage = (score / total) * 100

    st.write(f"👤 Player: **{st.session_state.player_name}**")
    st.write(f"✅ Score: **{score}/{total}**")
    st.write(f"📊 Percentage: **{percentage:.2f}%**")

    if st.button("Restart Quiz"):
        st.session_state.clear()
        st.rerun()