Feature: search for best earbuds in amazon

  Scenario Outline: user search for earbuds in amazon
    Given user is on "<site>"
    Then user search for earbuds
    And user checks with microphone and wireless box
    Then open each earbud link
    Then get required data
    Then connect to database
    And update data in table

    Examples:
      | site                   |
      | https://www.amazon.in/ |

#  Scenario: Analysing crawled data
#    Given table is updated
#    And create dataframe of table
