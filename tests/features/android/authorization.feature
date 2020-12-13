@android
@authorization
Feature: Authorization
  As Android device user I should be able to register and login to application only with a correct credentials

  @authorization_1
  Scenario: Email login
    Given [Android] I go to test environment as Unlogged user
      And [Android] Search by Image page is presented
     When [Android] I click "Me" tab
      And [Android] I login to application with correct credentials
     Then [Android] correct user nickname is presented on the header of the page
