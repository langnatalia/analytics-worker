const logger = require('./logger');
const { parse } = require('csv-parse');
const { Transform } = require('stream');

class Parser {
  constructor(options) {
    this.options = options;
    this.transformStream = new Transform({
      objectMode: true,
      transform: (chunk, encoding, callback) => {
        try {
          const parsedData = this.parseChunk(chunk);
          callback(null, parsedData);
        } catch (error) {
          logger.error('Error parsing chunk:', error);
          callback(error);
        }
      }
    });
  }

  parseChunk(chunk) {
    return new Promise((resolve, reject) => {
      parse(chunk, this.options, (err, data) => {
        if (err) {
          reject(err);
        } else {
          resolve(data);
        }
      });
    });
  }

  parseFile(filePath) {
    const fs = require('fs');
    const readStream = fs.createReadStream(filePath);
    const writeStream = fs.createWriteStream(`${filePath}.parsed`);

    readStream
      .pipe(this.transformStream)
      .pipe(writeStream)
      .on('finish', () => {
        logger.info(`Finished parsing file: ${filePath}`);
      })
      .on('error', (error) => {
        logger.error(`Error parsing file: ${filePath}`, error);
      });
  }
}

module.exports = Parser;