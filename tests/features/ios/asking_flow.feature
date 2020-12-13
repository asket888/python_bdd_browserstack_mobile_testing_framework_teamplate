@ios
@asking_flow
Feature: Asking Flow
  As IOS device user I should be able to Ask a new questions and Edit them

  @asking_flow_1
  Scenario: Ask Question
    Given [IOS] I go to test environment as Logged user
      And [IOS] Search by Image page is presented
     When [IOS] I click "Search by text" button
      And [IOS] I search for "[Mobile]" in the searching field
      And [IOS] I click "Ask question" button on Search page
     Then [IOS] "Ask your question" page is presented
     When [IOS] I add "[Mobile]" text and 20 random symbols to the text block on Add Question page
      And [IOS] I select "Matimatics" subject in the Subjects list
      And [IOS] I click "Ask question" button on Add Question page
      And [IOS] I choose "Ask Community" on Add Question page
     Then [IOS] "Asked question" page is presented
