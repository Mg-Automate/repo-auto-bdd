Feature: Logger Search functionality

    Scenario: Search using phone number
      Given user is on the login page of chathistory
      When user enters valid username "Manappuramtesting@pravid.io" and valid password "@#123Manappuram"
      And click on login button
      And select Logger tab
      And Select Date Range
      And click on search button and search by phone number "8123697283"
      Then Logger data should be for provided number


    Scenario: Search using loan ID
      Given user is on the login page of chathistory
      When user enters valid username "Manappuramtesting@pravid.io" and valid password "@#123Manappuram"
      And click on login button
      And select Logger tab
      And Select Date Range
      And click on search button and search by loan ID "Testing11"
      Then Logger data should be for provided loan ID