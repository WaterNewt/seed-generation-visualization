
# Seed generation visualization
![](https://www.gnu.org/graphics/gplv3-or-later-sm.png)

This is a very simple visualization of seed generation. It uses `pygame` for visualization, and the built-in `random` module for seed randomizing.

## Configuration
In the root directory of the project, there's a `GENERATION.env` configuration file. This is what it should look like by default:
```python
SEED=None
```
If the `SEED` value is set to `None`, it will generate the seed randomly when the script is ran.

If you want a set seed (let's say 42), you would have to change the `SEED` value to the seed you want (in this case, it's `42`). It would look something like this:
```python
SEED=42
```

## Setup
First, you want to install the required dependencies (`pygame` and `dotenv`). You can do this by running this command:
```zsh
pip3 install -r requirements.txt
```
If this command results in an error, you can install the packages manually, by typing this command:
```zsh
pip3 install pygame python-dotenv
```

## Running the script
Run this command, to run the script:
```zsh
python3 main.py
```

## Conclusion
If you encounter any errors/problems in any of these steps, please write an issue on this repository.