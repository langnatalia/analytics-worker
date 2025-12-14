package analytics

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/google/uuid"
)

// ErrorResponse represents an error response
type ErrorResponse struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
}

// NewErrorResponse returns a new error response
func NewErrorResponse(code int, message string) *ErrorResponse {
	return &ErrorResponse{
		Code:    code,
		Message: message,
	}
}

// HandleError handles an error and returns an error response
func HandleError(w http.ResponseWriter, err error) {
	log.Println(err)
	http.Error(w, err.Error(), http.StatusInternalServerError)
}

// WriteJSON writes a JSON response
func WriteJSON(w http.ResponseWriter, data interface{}) error {
	jsonData, err := json.Marshal(data)
	if err != nil {
		return err
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(jsonData)
	return nil
}

// GenerateUUID generates a new UUID
func GenerateUUID() string {
	return uuid.New().String()
}

// GetTimestamp returns the current timestamp
func GetTimestamp() int64 {
	return time.Now().UnixNano() / int64(time.Millisecond)
}

// CheckTimeout checks if a timeout has occurred
func CheckTimeout(start time.Time, timeout time.Duration) bool {
	return time.Since(start) > timeout
}

// GetHeader returns the value of a header
func GetHeader(r *http.Request, key string) string {
	return r.Header.Get(key)
}

// ValidateRequest validates a request
func ValidateRequest(r *http.Request) error {
	if r.Method != http.MethodPost {
		return errors.New("invalid request method")
	}
	if r.Header.Get("Content-Type") != "application/json" {
		return errors.New("invalid content type")
	}
	return nil
}

// LogRequest logs a request
func LogRequest(r *http.Request) {
	log.Printf("%s %s %s", r.Method, r.URL, r.RemoteAddr)
}