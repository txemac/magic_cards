# Cards

Using **only** the https://api.magicthegathering.io/v1/cards endpoint from the Magic the Gathering API and without using any query parameters for filtering, create a command-line tool that:

* Returns a list of **Cards** grouped by **`set`**.
* Returns a list of **Cards** grouped by **`set`** and then each **`set`** grouped by **`rarity`**.
* Returns a list of cards from the  **Khans of Tarkir (KTK)** that ONLY have the colours `red` AND `blue` (same results as https://api.magicthegathering.io/v1/cards?set=KTK&colors=Red,Blue)

## Environment

* You can use any one of the following programming languages: Ruby, Elixir, JavaScript, Crystal, Python, Go.

## Limitations

* You are **not** allowed to use a third-party library that wraps the MTG API.
* You can only use the https://api.magicthegathering.io/v1/cards endpoint for fetching all the cards. You **can't use query parameters** to filter the cards.

## What we look for

* Readability. Simplicity.
* Separation of Concerns.
* Avoid unnecessary abstractions.
* Great naming. We know _naming things_ is one of the two hardest problems in programming, so try to not make your solution too cryptic or too clever.
* Adherence to your language/framework conventions. No need to get _too_ creative._
* Comprehensive testing. _TDD is dead?_ No problem. Just make sure your bases are covered.
* Take your time, measure twice and cut once. Let us know roughly how much time you've spent.

## Bonus points for...

* Using only the programming language's standard library.
* **Parallelising** the retrieval of all the **Cards**  to speed up things.
* Respecting the API's Rate Limiting facilities.


# Environment
Python >= 3.8
* At root folder: create environment, activate and install requirements.
```shell script
virtualenv env
source env/bin/activate
pip install -r requiremets.txt
```

# Test
In the environment
```shell script
py.test -vvv
```

# Run
* List of cards grouped by set:
```shell script
python main.py
```

And select the option 'a', 'b' or 'c'.
Select m if you want see the total result.
