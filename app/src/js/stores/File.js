import { EventEmitter } from "events";

import dispatcher from "../dispatcher.js";

import localStorage from "localStorage";

class FileStore extends EventEmitter {

    constructor() {
        super();
        this.store = { file: null, newFile: false };
    }

    getAll() {
        return this.store;
    }

    getFile() {
        return this.store.file;
    }

    getNewFile() {
        return this.store.newFile;
    }

    updateNew() {
        console.log("updating");
        if (this.store.newFile == false) {
            this.store.newFile = true;
        } else {
            this.store.newFile = false;
        }
        this.emit("change");
    }

    storeFile(file) {
        this.store.file = file;
        this.emit("change");
    }

    handleAction(action) {
        switch(action.type) {
            case "STORE_FILE": {
                this.storeFile(action.file);
                break;
            }
            case "UPDATE_NEW": {
                this.updateNew();
                break;
            }

        }
    }

}

const fileStore = new FileStore;

dispatcher.register(fileStore.handleAction.bind(fileStore));

export default fileStore;
