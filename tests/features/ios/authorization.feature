@ios
@authorization
Feature: Authorization
  As IOS device user I should be able to register and login to application only with a correct credentials

  @authorization_1
  Scenario: Email login
    Given [IOS] I go to test environment as Unlogged user
      And [IOS] Search by Image page is presented
     When [IOS] I click "Profile" tab
      And [IOS] I login to application with correct credentials
     Then [IOS] correct user nickname is presented on the header of the page
