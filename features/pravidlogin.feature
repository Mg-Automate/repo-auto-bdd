Feature: Login pravid
    Scenario: Log in to pravid
      Given user is on the login page of pravid
      When user enters valid username "adminUser@InternalTesting.com" and valid password "InternalTesting@1234"
      And click on login button
      Then the user is logged in


      Scenario Outline: Log in to pravid with multiple users
      Given user is on the login page of pravid
      When user enters valid username "<username>" and valid password "<password>"
      And click on login button
      Then the user is logged in
        Examples:
          |username|password|
          |adminUser@InternalTesting.com|InternalTesting@123|
          |Chqbookadmin@pravid.io       |Chqbook@#456       |
          |manappuramadmin@pravid.io    |ManaPpuram@123     |
          |Prodtesting@pravid.io        |Testing@#456       |