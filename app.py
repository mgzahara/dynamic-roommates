from flask import Flask, render_template, request
app = Flask(__name__)

resident_questions = [] # questions for residents
meta = dict() # meta info for resident questions - name, age, etc.
question_specs = [] # all info for each question

#server root
@app.route('/')
def home():
    # placeholder - does nothing
    print "rendering home"
    return render_template('home.html')


@app.route('/set_up')
def about():
    # prompt user for questions topose to residents
    print "rendering set up"
    return render_template('set_up.html', questions = resident_questions, len = len(resident_questions))


@app.route('/questions_in', methods=['POST'])
def questions_in():
    # store provided questions, prompt for answers to each question
    global resident_questions
    arr = request.form['resident_questions']
    arr = arr.splitlines()
    resident_questions = [s.strip() for s in arr if s.strip() != "" ]
    return  render_template('set_up_phase2.html', questions = resident_questions, len = len(resident_questions))


@app.route('/answers_in', methods=['POST'])
def answers_in():
    # get answer options for each question, send to another page for validation
    global meta
    global question_specs
    global resident_questions

    question_specs = []
    
    print "/answers_in"
    print

    # get truth values of 'meta' info from checkboxes
    meta["name"] = request.form.get("get_name") != None
    meta["gender"] = request.form.get("get_gender") != None
    meta["id"] = request.form.get("get_id") != None
    meta["age"] = request.form.get("get_age") != None

    for i in range(len(resident_questions)):
        # for each question: get checkboxes/radio buttons values

        #element names are dynamic, hence the code below
        keys = ["req", "choice", "ans"]
        keys = [k + str(i) for k in keys]

        specs = dict(req = request.form.get(keys[0]) != None,
                     single_choice = request.form.get(keys[1]) == "single"
                    )
        # get and clean up possible answers
        unclean_ans = request.form[keys[2]]
        unclean_ans = unclean_ans.splitlines()
        specs["ans"] = [s.strip() for s in unclean_ans if s.strip() != ""]
        question_specs.append(specs)

    # give the necessary template the arrays and dict to work with
    return render_template('set_up_phase3.html', questions = resident_questions, specs = question_specs, meta = meta)

@app.route('/contact')
def contact():
    # placeholder
    return render_template('contact.html')

@app.route('/other')
def other():
    # placeholder
    return render_template('other.html')

#start app
if __name__ == "__main__":
    app.run(debug=True)
