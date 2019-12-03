Personal Solutions for AoC 2019
===============================

See `template.py` for an example of setting up a solution.

Solution filenames should take the form of `day_##.py`. The day number is parsed from the filename and used to download the puzzle input to the `.\data` folder.

To auto download puzzle input an `env.json` with a session cookie is required, i.e.

```json
{
  "session": "####"
}
```

The session cookie can be viewed from a browser developer tools, and is the only cookie set by AoC.