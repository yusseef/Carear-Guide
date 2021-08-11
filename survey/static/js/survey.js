const question = document.querySelector('#question')
const choices = Array.from(document.querySelectorAll('.choice-text'))

let currentQuestion = {}
let acceptingAnswers = true
let questionCounter = 0
let availableQuestions = []
let score = []

let questions = [
    {
        question: 'I like to do puzzles',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'I'

    },
    {
        question: 'I am good at working independently',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'A'

    },
    {
        question: 'I like to work in teams',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes', 
        cat:'S'

    },
    {
        question: 'I am an ambitious person, I set goals for myself',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'E', 

    },
    {
        question: 'I pay attention to details',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes', 
        cat:'C'

    },
    {
        question: 'I like to try to influence or persuade people',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes', 
        cat:'E'

    },
    {
        question: 'I like trying to help people solve their problems',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes', 
        cat:'R'

    },
    {
        question: 'I enjoy creative writing',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes', 
        cat:'A'

    },
    {
        question: 'I enjoy science',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'I'

    },
    {
        question: 'I like putting things together or assembling things',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes', 
        cat:'R'

    },
    {
        question: 'I am good at keeping records of my works',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'C'

    },
    {
        question: 'I am a creative person',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'A'

    },
    {
        question: 'I enjoy learning about other cultures',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'S'

    },
    {
        question: 'I would like to start my own business',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'E'

    },
    {
        question: 'I am a practical person',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'R'

    },
    {
        question: 'I like working with numbers or charts',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'I'

    },
    {
        question: 'I like to get into discussions about issues',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'S'

    },
    {
        question: 'I like to lead',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'E'

    },
    {
        question: 'I like to organize things, (files, desks/offices)',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'C'

    },
    {
        question: 'I like working outdoors',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'R'

    },
    {
        question: 'I like to draw',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'A'

    },
    {
        question: 'I like to do experiments',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'I'

    },
    {
        question: 'I like to teach or train people',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'S'

    },
    {
        question: 'I would like to work in an office',
        choice1: 'Yes',
        choice2 : 'No',
        answer:'Yes',
        cat:'C'

    },
 

]