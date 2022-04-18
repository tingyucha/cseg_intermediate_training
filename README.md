# CSEG git practice repo

The aim here is to practice or learn some basic git commands in a functional (albeit very simple) code base.

In the steps below you'll cover `add` `commit` `checkout` `branch` `push` `merge` `log` `reset`.

## Basics setup of the script.
At the top of the script are some doctest.  Lines that start with `>>>` will be tested to match the following line.  As you add functions, uncomment the `#>>>` lines to `>>>` to make sure the code works.
The aim here is git commands though, not python code.
To run the tests execute:

    python -m doctest temp_converter.py

No output means things worked. For verbose output add `-v`

    python -m doctest -v temp_converter.py


The bottom of the script has very a simple CLI, which we'll add functionality to.  To start run simply with a numeric input value:

    python temp_converter.py 23.2



## Tasks:

### Task 1:

To start we'll add a `celcius_to_fahrenheit` function to the script.  To do this, we'll first create a new branch.  This can be a "feature branch" as we add a new feature to the code.

    git checkout -b feature

`git checkout` changes to an alternate branch, or commit or tag.  Usually you'll use it for switching branches.
`-b` will create and checkout a new branch

<br>
<br>

From this point we can make our code edits, replace the current `place_holder()` function with your new `celcius_to_fahrenheit()`. when we're happy we'll "stage" the edits using

    git add temp_converter.py

If we're happy and want to "commit" to the edits, we can add a comment for the log.

    git commit -m "add C to F function"

To backup or share these local edits, we can now `push` to the remote repository.

    git push

<br>
<br>

<details>
    <summary>Full commands for task 1</summary>

    git checkout -b feature1

    def celcius_to_fahrenheit(celcius):
        return (celcius * 9/5) + 32

    python -m doctest temp_converter.py
    python temp_converter.py 68

    git add temp_converter.py
    git commit -m "add C to F function"
    git push
</details>

<hr>
<br>
<br>

### Task 1 wrapup

Now lets go back to our main branch.  We don't need to create this time so just checkout with no flags.

Let's take a look at `git status` to see which branch we're on, and `git log` to see the history.

Take a look at your file.  It should have reverted back to the original.  You can switch back and forth to the new branch now wih checkout and your branch name.

<details>
    <summary>Full commands for task 1 wrap up</summary>

    git checkout main
    git checkout feature1
    git status
    git log
</details>


<hr>
<hr>
<br>
<br>

### Task 2:
Make sure we're back on `main` branch before starting.  Let's create another new feature branch.  Name it `feature2` or whatever you want.

This time let's add a `celcius_to_kelvin`, like before replace the `place_holder()` with your new function and then add another `kelvin_to_celcius` function.  Your file at this time should not support `celcius_to_fahrenheit` that's still on `feature1` only.

When the code is done, `add` the file to `stage` the edits and if happy `commit` the edits with a useful comment.

Check the `status` of where we're at and then let's `push` up to github again.

<details>
    <summary>Full commands for task 2</summary>

    git checkout main
    git checkout -b feature2
    ..edit code...
    git diff
    git status
    git add temp_converter.py
    git commit -m "add kelvin support"
    git status
    git push

</details>

<hr>
<hr>
<br>
<br>

### Task 3a:
Open up a PR for `feature1` branch on github.com.  Take a look at the changes, etc.
Then we'll `merge` this branch in to main.

On your local computer, `git checkout main` and `git pull` to see the remote changes.
Check the `log` to see how the history has been merged.

### Task 3b:
Back on github.com, open up another PR for `feature2` branch.  We should now run into a merge conflict.  Resolve the conflict through the browser, add a commit message about the merge.
The `main` branch should now include all 4 functions and the log should show a combined history.

On your local computer, use `git fetch`, `git status` and `git pull` to synchronize edits with the remote repo.

<details>
    <summary>Local commands for task 3</summary>

    git checkout main
    git diff feature1
    git merge feature1

    git diff feature2
    git merge feature2
    ... resolve conflict ...
    git commit -m "merge feature2 branch"
    git status
    git push

</details>

<hr>
<hr>
<br>
<br>

### Task 4a:
Still on the main branch, let's add the last 2 functions.  `fahrenheit_to_kelvin` and `kelvin_to_fahrenheit`.  When we're happy, `add` and `commit` those edits (Do Not Push).

Now, we've made edits directly to the `main` branch.  In big repos, this is a no-no, we want to make edits on branches which are reviewed and then merged.  That detail doesn't matter too much, but we want to undo those commit(s) but keep the work.

Check `git log` to see how many commits we want to "undo".  Then
`git reset HEAD~1` or `git reset <hash>`.
This will apply a `mixed` reset, where the edits are kept but unstaged and the commit is undone.
A `hard` reset undoes the edits as well, all progress is forgotten.
A `soft` reset keeps the edits and keeps them staged, similar to mixed.

Now `git status` should say we have "changes not staged for commit", let's create a `feature3` branch.  Then `add` and `commit` those changes to that branch.


### Task 4b:

The product team has decided that all temperatures will be in °Ré and that no conversions will be available.  Delete all the code, we don't want to maintain that and replace with a simple `print("Please use °Réaumur, no conversions provided")`.
`Add` and `commit` this very important change.

### Task 4c:

The product team had some coffee and realised the previous changes weren't optimal.  They would like all the previous functionality restored.
Use `git log` to check the commit hash or number of commits to undo, then `git reset --hard HEAD~1` or `git reset --hard <hash>`

To merge the extra functions into main again, open up a PR on github.com check the changes and merge.

<details>
    <summary>Full commands for task 4</summary>

    ...edit code...
    git add .
    git commit -m "add f to k support"
    git log
    git reset HEAD~1

    git checkout -b feature3
    git add .
    git commit -m "add f to k support"

    ...edit code...
    git add .
    git commit -m "purge all code only support °Réaumur"
    git log
    git reset --hard HEAD~1

    git checkout main
    git diff feature3
    git merge feature3
    git push

</details>

