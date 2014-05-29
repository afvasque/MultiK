package cl.test;


import java.text.SimpleDateFormat;
import java.util.Date;

import cl.registro.logic.Session;
import cl.registro.util.Persistencia;
import cl.test.util.SystemUiHider;

import android.annotation.TargetApi;
import android.app.Activity;
import android.content.Intent;

import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.os.Handler;
import android.os.SystemClock;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.Chronometer;

/**
 * An example full-screen activity that shows and hides the system UI (i.e.
 * status bar and navigation/system bar) with user interaction.
 * 
 * @see SystemUiHider
 */
public class RegistraDatosActivity extends Activity {
	/**
	 * Whether or not the system UI should be auto-hidden after
	 * {@link #AUTO_HIDE_DELAY_MILLIS} milliseconds.
	 */
	private static final boolean AUTO_HIDE = true;

	/**
	 * If {@link #AUTO_HIDE} is set, the number of milliseconds to wait after
	 * user interaction before hiding the system UI.
	 */
	private static final int AUTO_HIDE_DELAY_MILLIS = 3000;

	/**
	 * If set, will toggle the system UI visibility upon interaction. Otherwise,
	 * will show the system UI visibility upon interaction.
	 */
	private static final boolean TOGGLE_ON_CLICK = true;

	/**
	 * The flags to pass to {@link SystemUiHider#getInstance}.
	 */
	private static final int HIDER_FLAGS = SystemUiHider.FLAG_HIDE_NAVIGATION;

	/**
	 * The instance of the {@link SystemUiHider} for this activity.
	 */
	private SystemUiHider mSystemUiHider;
Session session;


String filePath;
	public static final String DATE_FORMAT="dd-MM-yyyy hh:mm:ss";
	static SimpleDateFormat simpleDateFormat=new SimpleDateFormat(DATE_FORMAT);
	 Intent i; 
	
	
	
	protected void onCreate(Bundle savedInstanceState) {
		
		super.onCreate(savedInstanceState);

		setContentView(R.layout.activity_registra_datos);

		Intent intent = getIntent();
	    String fileName = intent.getStringExtra(IniciarCapturaDatosActivity.FILE_NAME);

		final View contentView = findViewById(R.id.fullscreen_content);
		i= new Intent(this, IniciarCapturaDatosActivity.class);

		
		session=new Session();
		if(!fileName.contains(".xml")){
			fileName=fileName+".xml";
		}
      filePath =Environment.getExternalStorageDirectory().getPath()+"/"+fileName;
        session.setFechaHoraInicio(simpleDateFormat.format(new Date()));
        System.out.println("filePath["+filePath+"].");
        Log.i("filePath",filePath);
        super.onCreate(savedInstanceState);
     
      
    
      PresionaBotonListener presionaBotonListener=new PresionaBotonListener();
      presionaBotonListener.setSimpleDateFormat(simpleDateFormat);
      presionaBotonListener.setFilePath(filePath);

     
      presionaBotonListener.setSession(session);
      
      Chronometer cronometro = (Chronometer)findViewById(R.id.chronometer1);
      cronometro.start();

       // Hablar sobre el software (niño)
        findViewById(R.id.HSPH).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HSOH).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HSCH).setOnClickListener(presionaBotonListener);
       // Hablar sobre el software (niña)
        findViewById(R.id.HSPM).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HSOM).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HSCM).setOnClickListener(presionaBotonListener);
        
       // Hablar sobre contenido (niño)
        findViewById(R.id.HCPH).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HCOH).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HCCH).setOnClickListener(presionaBotonListener);
       // Hablar sobre contenido (niña)
        findViewById(R.id.HCPM).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HCOM).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HCCM).setOnClickListener(presionaBotonListener);
        
       // Hablar sobre otro tema (niño)
        findViewById(R.id.HOPH).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HOOH).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HOCH).setOnClickListener(presionaBotonListener);
       // Hablar sobre otro tema (niña)
        findViewById(R.id.HOPM).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HOOM).setOnClickListener(presionaBotonListener);
        findViewById(R.id.HOCM).setOnClickListener(presionaBotonListener);
        
       //Molestar a uno o varios compañeros
        findViewById(R.id.M1H).setOnClickListener(presionaBotonListener);
        findViewById(R.id.MVH).setOnClickListener(presionaBotonListener);
        findViewById(R.id.M1M).setOnClickListener(presionaBotonListener);
        findViewById(R.id.MVM).setOnClickListener(presionaBotonListener);
        
       //Distraerse sin disrupcion
        findViewById(R.id.DSDH).setOnClickListener(presionaBotonListener);
        findViewById(R.id.DSDM).setOnClickListener(presionaBotonListener);

		findViewById(R.id.boton_terminar).setOnClickListener(new OnClickListener() {
			   @Override
			   public void onClick(View v) {
				   session.setFechaHoraTermino(simpleDateFormat.format(new Date()));
				Persistencia.escribeInformacionSesion(session, filePath);
				   finishActivity(0);
                   startActivity(i);
			   }
			  });
			
		
		
		/**
		 * 
		 * FIN
		 * 
		 * **/
		// Set up an instance of SystemUiHider to control the system UI for
		// this activity.
		mSystemUiHider = SystemUiHider.getInstance(this, contentView,
				HIDER_FLAGS);
		mSystemUiHider.setup();
		mSystemUiHider
				.setOnVisibilityChangeListener(new SystemUiHider.OnVisibilityChangeListener() {
					// Cached values.
					int mControlsHeight;
					int mShortAnimTime;

					@Override
					@TargetApi(Build.VERSION_CODES.HONEYCOMB_MR2)
					public void onVisibilityChange(boolean visible) {
						if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB_MR2) {
							
							if (mControlsHeight == 0) {
								mControlsHeight = contentView.getHeight();
							}
							if (mShortAnimTime == 0) {
								mShortAnimTime = getResources().getInteger(
										android.R.integer.config_shortAnimTime);
							}
							contentView
									.animate()
									.translationY(visible ? 0 : mControlsHeight)
									.setDuration(mShortAnimTime);
						} else {
							// If the ViewPropertyAnimator APIs aren't
							// available, simply show or hide the in-layout UI
							// controls.
							contentView.setVisibility(visible ? View.VISIBLE
									: View.GONE);
						}

						if (visible && AUTO_HIDE) {
							// Schedule a hide().
							delayedHide(AUTO_HIDE_DELAY_MILLIS);
						}
					}
				});

		// Set up the user interaction to manually show or hide the system UI.
		contentView.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View view) {
				if (TOGGLE_ON_CLICK) {
					mSystemUiHider.toggle();
				} else {
					mSystemUiHider.show();
				}
			}
		});

		// Upon interacting with UI controls, delay any scheduled hide()
		// operations to prevent the jarring behavior of controls going away
		// while interacting with the UI.
		
	}

	@Override
	protected void onPostCreate(Bundle savedInstanceState) {
		super.onPostCreate(savedInstanceState);

		// Trigger the initial hide() shortly after the activity has been
		// created, to briefly hint to the user that UI controls
		// are available.
		delayedHide(100);
	}

	/**
	 * Touch listener to use for in-layout UI controls to delay hiding the
	 * system UI. This is to prevent the jarring behavior of controls going away
	 * while interacting with activity UI.
	 */
	View.OnTouchListener mDelayHideTouchListener = new View.OnTouchListener() {
		@Override
		public boolean onTouch(View view, MotionEvent motionEvent) {
			if (AUTO_HIDE) {
				delayedHide(AUTO_HIDE_DELAY_MILLIS);
			}
			return false;
		}
	};

	Handler mHideHandler = new Handler();
	Runnable mHideRunnable = new Runnable() {
		@Override
		public void run() {
			mSystemUiHider.hide();
		}
	};

	/**
	 * Schedules a call to hide() in [delay] milliseconds, canceling any
	 * previously scheduled calls.
	 */
	private void delayedHide(int delayMillis) {
		mHideHandler.removeCallbacks(mHideRunnable);
		mHideHandler.postDelayed(mHideRunnable, delayMillis);
	}
	   
}
