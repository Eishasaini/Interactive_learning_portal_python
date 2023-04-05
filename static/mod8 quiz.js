const quizData = [
    {
        question: "To read two characters from a file object infile, we use ____________",
        a: "infile.read(2)",
        b: "infile.read()",
        c: "infile.readline()",
        d: "infile.readlines()",
        correct: "a",
    },
    {
        question: "To read the next line of the file from a file object infile, we use ____________",
        a: "infile.read(2)",
        b: "infile.read()",
        c: "infile.readline()",
        d: "infile.readlines()",
        correct: "c",
    },
    {
        question: "The readlines() method returns ____________?",
        a: "str",
        b: "a list of lines",
        c: "a list of single characters",
        d: "a list of integers",
        correct: "b",
    },
    {
        question: "To read the entire remaining contents of the file as a string from a file object infile, we use?",
        a: "infile.read(2)",
        b: "infile.read()",
        c: "infile.readline()",
        d: "infile.readlines()",
        correct: "b",
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