# Repository Summary

Source reviewed: `https://github.com/rasch/imgur-cli`

## Files

- `README.md`: documents two commands, `imgur <url|path>` and `imgur del <deletehash>`.
- `package.json`: package name is `@rasch/imgur-cli`, version `0.1.0`, and the executable is the `imgur` bin pointing at `imgur.js`.
- `imgur.js`: full implementation in a single Node script with no runtime dependencies.

## Implementation Notes

- Uses Node built-ins only: `process`, `fs`, `https`, and `querystring`.
- Talks to `https://api.imgur.com/3/image`.
- Uses `POST /3/image` for uploads and `DELETE /3/image/<deletehash>` for deletions.
- Reads `IMGUR_CLIENTID` from the environment and falls back to a baked-in anonymous client ID.
- Accepts either:
  - a string starting with `http` and uploads by URL
  - an existing local file path and uploads its base64 contents
- Prints errors to stderr and exits non-zero for missing input, missing deletehash, or missing files.

## Local Install In This Environment

- Local clone: `/Users/eric_yiru/src/imgur-cli`
- Installed binary: `/Users/eric_yiru/.local/bin/imgur`
- Installed from the local clone with:

```bash
npm install --global --prefix /Users/eric_yiru/.local /Users/eric_yiru/src/imgur-cli
```
