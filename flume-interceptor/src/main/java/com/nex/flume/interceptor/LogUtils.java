package com.nex.flume.interceptor;

public class LogUtils {

    public static boolean validateEvent(String log) {
        if (log == null) {
            return false;
        }
        return log.trim().startsWith("{") && log.trim().endsWith("}");

    }
}
