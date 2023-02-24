import axios from "axios";
import { Client } from "revolt.js";

let client = new Client();
require("dotenv").config();

const prefix = ".";

client.on("ready", async () =>
  console.info(`Logged in as ${client.user!.username}!`)
);

client.on("message", async (message) => {
  const args = message.content?.slice(prefix.length).split(/ +/);
  const command = args?.shift()?.toLowerCase();

  if (command === "prompt") {
    await axios
      .post("http://localhost:8000/prompt", {
        input: message.content!.slice(command.length).replace("t ", ""),
      })
      .then((res) => {
        message.channel!.sendMessage(res.data.output);
      });
  }
});

const token = process.env.BOT_TOKEN;
// @ts-ignore
client.loginBot(token);
