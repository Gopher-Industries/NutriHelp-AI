import firebase from "firebase/compat/app";
import "firebase/compat/auth";
import "firebase/compat/firestore";

const firebaseConfig = {
  apiKey: "<Input API Key>",
  authDomain: "sit-22t3-team-task-for-137936f.firebaseapp.com",
  projectId: "sit-22t3-team-task-for-137936f",
  storageBucket: "sit-22t3-team-task-for-137936f.appspot.com",
  messagingSenderId: "265422758991",
  appId: "1:265422758991:web:cbe15f904993256f8df63a",
};

if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}
export { firebase };
