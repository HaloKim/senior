package com.example.spotdifference;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.view.View;

public class MyDrawEx extends View {
    public MyDrawEx(Context c){
        super(c);
    }

    public MyDrawEx(Context c, AttributeSet a) {
        super(c,a);
    }
    public MyDrawEx(Context c,AttributeSet a, int ref) {
        super(c,a,ref);
    }

    @Override
    public void onDraw(Canvas c){
        Paint paint = new Paint();
        paint.setStyle(Paint.Style.FILL);
        c.drawColor(Color.WHITE);
        paint.setColor(Color.BLUE);
        c.drawCircle(20,20,15,paint);
    }
}
