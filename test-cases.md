# Test Cases - SauceDemo

| Test Case ID | Title                     | Steps                                                                 | Expected Result                                | Status |
|--------------|---------------------------|-----------------------------------------------------------------------|------------------------------------------------|--------|
| TC01         | Login with valid data     | Enter `standard_user` / secret_sauce, click Login                     | Redirects to products page                     | Pass   |
| TC02         | Login with invalid user   | Enter wrong_user / secret_sauce, click Login                          | Shows error message                            | Pass   |
| TC03         | Add item to cart          | Click "Add to cart" on 1st product                                    | Button changes to "Remove", cart icon updates  | Pass   |
| TC04         | Remove item from cart     | Click "Remove" button in cart                                         | Item removed, counter decrements               | Pass   |
| TC05         | Sort A–Z products         | Select "Name (A to Z)" from sort dropdown                             | Products ordered alphabetically (A–Z)          | Pass   |
| TC06         | Checkout with empty cart  | Go to cart and click Checkout with no items                           | Blocked or error shown                         | Pass   |
