const collectionPath = "2321sadas";
const rootUrl = new URL("./", document.baseURI);
const elements = {
  list: document.querySelector("#program-list"),
  collectionTitle: document.querySelector("#collection-title"),
  programs: document.querySelector("#programs"),
  viewer: document.querySelector("#program-viewer"),
  programTitle: document.querySelector("#program-title"),
  backLink: document.querySelector("#back-link"),
  copyButton: document.querySelector("#copy-button"),
  copyStatus: document.querySelector("#copy-status"),
  sourceCode: document.querySelector("#source-code"),
  error: document.querySelector("#error-message"),
};

function showError(message) {
  elements.error.textContent = message;
  elements.error.hidden = false;
  elements.list.hidden = true;
  elements.viewer.hidden = true;
}

function routeParts() {
  const pathname = decodeURIComponent(window.location.pathname);
  const rootPath = decodeURIComponent(rootUrl.pathname);
  if (!pathname.startsWith(rootPath)) {
    return null;
  }
  return pathname.slice(rootPath.length).split("/").filter(Boolean);
}

function showPrograms(collection) {
  elements.collectionTitle.textContent = collection.id;
  elements.programs.replaceChildren();

  for (const program of collection.programs) {
    const item = document.createElement("li");
    const link = document.createElement("a");
    link.href = new URL(`${collection.id}/${program.id}/`, rootUrl).href;
    link.textContent = program.title;
    item.append(link);
    elements.programs.append(item);
  }

  elements.list.hidden = false;
}

async function copySource() {
  const source = elements.sourceCode.textContent;
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(source);
    } else {
      copyWithFallback(source);
    }
    elements.copyStatus.textContent = "Copied!";
  } catch {
    try {
      copyWithFallback(source);
      elements.copyStatus.textContent = "Copied!";
    } catch {
      elements.copyStatus.textContent = "Could not copy the code. Select and copy it manually.";
    }
  }
}

function copyWithFallback(source) {
  const textarea = document.createElement("textarea");
  textarea.value = source;
  textarea.setAttribute("readonly", "");
  textarea.style.position = "fixed";
  textarea.style.opacity = "0";
  document.body.append(textarea);
  textarea.select();
  const copied = document.execCommand("copy");
  textarea.remove();
  if (!copied) {
    throw new Error("Clipboard copy was not available.");
  }
}

async function showProgram(collection, programId) {
  const program = collection.programs.find((item) => item.id === programId);
  if (!program) {
    showError(`Program "${programId}" was not found in collection ${collection.id}.`);
    return;
  }

  elements.programTitle.textContent = program.title;
  elements.backLink.href = new URL(`${collection.id}/`, rootUrl).href;
  elements.copyButton.addEventListener("click", copySource);
  elements.viewer.hidden = false;

  try {
    const response = await fetch(new URL(program.file, rootUrl));
    if (!response.ok) {
      throw new Error(`The source file could not be loaded (HTTP ${response.status}).`);
    }
    elements.sourceCode.textContent = await response.text();
  } catch (error) {
    showError(error instanceof Error ? error.message : "The source file could not be loaded.");
  }
}

async function start() {
  let parts;
  try {
    parts = routeParts();
  } catch {
    showError("This URL is not valid.");
    return;
  }

  if (!parts || (parts.length > 0 && parts[0] !== collectionPath) || parts.length > 2) {
    showError("This LabCode page was not found.");
    return;
  }

  let collections;
  try {
    const response = await fetch(new URL("data/collections.json", rootUrl), { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Collections could not be loaded (HTTP ${response.status}).`);
    }
    collections = await response.json();
  } catch (error) {
    showError(error instanceof Error ? error.message : "Collections could not be loaded.");
    return;
  }

  const collection = collections.find((item) => item.id === collectionPath);
  if (!collection) {
    showError(`Collection "${collectionPath}" was not found.`);
    return;
  }

  if (parts.length === 2) {
    await showProgram(collection, parts[1]);
  } else {
    showPrograms(collection);
  }
}

start();
