Feature: Pravid Logo
  Scenario: Logo presence on Pravid home page
    Given lauch chrome
    When open pravid home page
    Then verify logo present on page
    And close browser