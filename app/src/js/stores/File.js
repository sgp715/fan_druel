import { EventEmitter } from "events";

import dispatcher from "../dispatcher.js";

// import localStorage from "localStorage";

class FileStore extends EventEmitter {

    constructor() {
        super();
        this.store = { file: null };
    }

    getAll() {
        return this.store.file;
    }

    updateFile(file) {

        if (this.store.file == null) {
            this.store.file = file;
        }
        else {
            this.store.file = null;
        }
        this.emit("change");
    }

    handleAction(action) {
        switch(action.type) {
            case "UPDATE_FILE": {
                this.updateFile(action.file);
                break;
            }
        }
    }

}

const fileStore = new FileStore;

dispatcher.register(fileStore.handleAction.bind(fileStore));

export default fileStore;
