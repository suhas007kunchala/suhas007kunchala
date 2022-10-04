Feature: TS_103 login into yourlogo

  Scenario Outline: TC_103 login
    Given yourlogo website "<site>" is opened
    When sign in button is clicked
    Then use "<email>" to enter email
    Then use "<password>" to enter password
    Then click on sign in button
    Then validate login success
    And user clicks sign out

    Examples:
      | site | email         | password |
      | http://automationpractice.com/index.php     | gm63@live.com | lkjh1234 |

  Scenario: TC_104 Add-to-cart
    Given user is on home page
    When user clicks on "women" module
    Then user checks tops checkbox
    And user selects "In stock" option
    And user slides low to "20" and high to "-40"
    When user hovers over product
    Then user clicks on quick view
    And user selects "1" size option
    And user clicks on Add to cart
    Then user clicks on Proceed to checkout
    Then user checks "summary" and clicks on checkout
    Then user checks Delivery "address" and clicks on checkout
    And user checks i agree in "shipping" details and click on checkout
    Then user clicks on Pay by bank wire
    Then user clicks on I confirm my order
    And user should see order complete message
    Then user clicks on Home button
    Then user vists yourlogo twitter page
    Then user clicks on follow button
    Then user navigates back to yourlogo page
    Then user logout from yourlogo website






