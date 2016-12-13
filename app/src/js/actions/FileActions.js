import dispatcher from "../dispatcher.js";

export function storeFile(file) {
    dispatcher.dispatch({
        type: "STORE_FILE",
        file: file
    });
}

export function updateNew() {
    dispatcher.dispatch({
        type: "UPDATE_NEW"
    });
}
