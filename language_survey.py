from survey import AnonymousSurvey

question = "最初に勉強した言語はなんですか？"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("'q'を入力すると終了します\n")
while True:
    response = input("言語: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nアンケート調査にご協力ありがとうございます！")
my_survey.show_results()