@ios
@search_flow
Feature: Search and filter
  As IOS device user I should be able to search and filter questions

  @search_flow_1
  Scenario: Search by Text
    Given [IOS] I go to test environment as Unlogged user
      And [IOS] Search by Image page is presented
     When [IOS] I click "Search by text" button
      And [IOS] I search for "English" in the searching field
     Then [IOS] Search results block is presented on the page
      And [IOS] "10" results are presented in search results on the page
     When [IOS] I click first question in the list on Search page
     Then [IOS] question page is presented
