// types.ts
// eslint-disable-next-line @typescript-eslint/no-empty-interface
export interface AnalyticsWorkerOptions {
  /**
   * The file path to the analytics data file.
   */
  filePath: string;
  /**
   * The worker name, used for logging and debugging purposes.
   */
  workerName: string;
  /**
   * A callback function to handle errors.
   */
  onError: (err: Error) => void;
  /**
   * A callback function to handle completed tasks.
   */
  onComplete: () => void;
}

export interface AnalyticsTask {
  id: string;
  data: object;
  options: AnalyticsWorkerOptions;
}