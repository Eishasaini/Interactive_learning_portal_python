const quizData = [
    {
        question: "Which of the following is the use of function in python?",
        a: "Functions are reusable pieces of programs",
        b: "Functions don’t provide better modularity for your application",
        c: "you can’t also create your own functions",
        d: " All of the mentioned above",
        correct: "a",
    },
    {
        question: "Which keyword is used for function?",
        a: "Fun",
        b: "Define",
        c: "Def",
        d: "Function",
        correct: "c",
    },
    {
        question: "A lambda function in Python can take __________.",
        a: "only one argument",
        b: "only two arguments",
        c: "only three arguments",
        d: "any number of arguments",
        correct: "d",
    },
    {
        question: "Lambda is a function in python?",
        a: "True",
        b: "False",
        c: "lambda is a function in python but user cannot use it",
        d: "none of the above",
        correct: "a",
    },


];

const quiz= document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const a_text = document.getElementById('a_text')
const b_text = document.getElementById('b_text')
const c_text = document.getElementById('c_text')
const d_text = document.getElementById('d_text')
const submitBtn = document.getElementById('submit')


let currentQuiz = 0
let score = 0

loadQuiz()

function loadQuiz() {

    deselectAnswers()

    const currentQuizData = quizData[currentQuiz]

    questionEl.innerText = currentQuizData.question
    a_text.innerText = currentQuizData.a
    b_text.innerText = currentQuizData.b
    c_text.innerText = currentQuizData.c
    d_text.innerText = currentQuizData.d
}

function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false)
}

function getSelected() {
    let answer
    answerEls.forEach(answerEl => {
        if(answerEl.checked) {
            answer = answerEl.id
        }
    })
    return answer
}


submitBtn.addEventListener('click', () => {
    const answer = getSelected()
    if(answer) {
       if(answer === quizData[currentQuiz].correct) {
           score++
       }

       currentQuiz++

       if(currentQuiz < quizData.length) {
           loadQuiz()
       } else {
           quiz.innerHTML = `
           <h2>You answered ${score}/${quizData.length} questions correctly</h2>

           <button onclick="location.reload()">Reload</button>
           `
       }
    }
})