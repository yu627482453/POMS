package com.nex.flume.interceptor;

import org.apache.flume.Context;
import org.apache.flume.Event;
import org.apache.flume.interceptor.Interceptor;

import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class LogETLInterceptor implements Interceptor {


    @Override
    public void initialize() {

    }

    @Override
    public Event intercept(Event event) {

        byte[] body = event.getBody();
        String log = new String(body, Charset.forName("UTF-8"));

        if (LogUtils.validateEvent(log)) {
            return event;
        }

        return null;
    }

    @Override
    public List<Event> intercept(List<Event> list) {

        ArrayList<Event> interceptors = new ArrayList<>();

        for (Event event : list) {
            Event intercept1 = intercept(event);
            if (intercept1 != null) {
                interceptors.add(event);
            }
        }
        return interceptors;
    }

    @Override
    public void close() {

    }

    public static class Builder implements Interceptor.Builder {
        @Override
        public Interceptor build() {
            return new LogETLInterceptor();
        }

        @Override
        public void configure(Context context) {

        }
    }

}
