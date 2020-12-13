@android
@asking_flow
Feature: Asking Flow
  As Android device user I should be able to Ask a new questions and Edit them

  @asking_flow_1
  Scenario: Ask Question
    Given [Android] I go to test environment as Logged user
      And [Android] Search by Image page is presented
     When [Android] I click "Search by text" button
      And [Android] I search for "[Mobile]" in the searching field
      And [Android] I click "Ask question" button on Search page
     Then [Android] "Ask your question" page is presented
     When [Android] I add "[Mobile]" text and 20 random symbols to the text block on Add Question page
      And [Android] I click "Ask question" button on Add Question page
      And [Android] I select first subject in the Subjects list
     Then [Android] question page is presented
      And [Android] "Matimatics" subject is presented in question block on Question page
      And [Android] "[Mobile]" text is presented in question block on Question page
      And [Android] correct user name is presented in question block on Question page
