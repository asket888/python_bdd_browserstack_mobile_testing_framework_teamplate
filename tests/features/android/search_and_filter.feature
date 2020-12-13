@android
@search_flow
Feature: Search and filter
  As Android device user I should be able to search and filter questions

  @search_flow_1
  Scenario: Search by Text
    Given [Android] I go to test environment as Unlogged user
      And [Android] Search by Image page is presented
     When [Android] I click "Search by text" button
      And [Android] I search for "English" in the searching field
     Then [Android] Search results block is presented on the page
      And [Android] "English" keyword is presented in all search results on the page
     When [Android] I click first question in the list on Search page
     Then [Android] question page is presented
