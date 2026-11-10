# LabCode

LabCode is a static Python code-sharing site. It serves Python source files as text and never runs them.

## Run locally

Use a local static web server from the repository root so browser `fetch()` requests work. For example, with Python installed:

```powershell
py -m http.server 8000
```

Open <http://localhost:8000/>. The collection is also available at <http://localhost:8000/2321sadas/>, and each program has its own URL such as <http://localhost:8000/2321sadas/program-1/>.

## Add or edit a program

1. Put the Python source in `codes/<collection-id>/<program-id>.py`.
2. Add its `id`, display `title`, and relative `file` path to `data/collections.json`.
3. For each new shareable program URL, add a directory at `<collection-id>/<program-id>/` containing an `index.html` based on one of the existing program route pages. Set its `<base href>` to `../../` so assets resolve from the site root.
4. For a new collection URL, add `<collection-id>/index.html` based on the existing collection route page, with `<base href="../">`, and update `collectionPath` in `script.js` if changing the active collection.

GitHub Pages is static hosting; it does not rewrite arbitrary paths. The route directories and their `index.html` files make the shareable URLs work on GitHub Pages without server-side routing. Keep the route pages' base path correct if you change their nesting.

## Deploy to GitHub Pages

GitHub Pages is the easiest option for this project. **Make the repository public** to ensure the published site and its source files can be viewed without a GitHub sign-in. Visitors do not need a GitHub account; only you need to sign in to create the repository and configure hosting.

1. Sign in to GitHub and create a **public** repository named `labcode`.
2. Upload all the project files and folders from this workspace to the repository root. Do not upload just `index.html`; the `data`, `codes`, and route folders are needed too.
3. In the repository, open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**, select the branch containing the site (usually `main`) and the `/ (root)` folder, then save.
5. Wait for the Pages deployment to finish. Your public site will be `https://<your-github-username>.github.io/labcode/`. Share these links:
   - Collection: `https://<your-github-username>.github.io/labcode/2321sadas/`
   - Programs: `https://<your-github-username>.github.io/labcode/2321sadas/program-1/` (replace `1` with `2`, `3`, or `4`)

Open the published links in a private/incognito browser window to confirm they work while signed out. Do not enable a Pages access restriction if GitHub offers one.

The included `.nojekyll` file asks GitHub Pages to serve the static files directly. The included `404.html` gives a useful response for unknown routes.

## Add a custom domain later

In **Settings → Pages**, enter the custom domain and follow GitHub's DNS instructions. Configure the required DNS records at your domain provider and enable HTTPS after GitHub verifies the domain. For a root/apex domain, GitHub typically requests `A`/`AAAA` records; for a subdomain such as `www`, it typically requests a `CNAME`. Keep the site's files at the repository root so its relative asset paths continue to work under the custom domain.
