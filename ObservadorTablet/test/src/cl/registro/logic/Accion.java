package cl.registro.logic;




public class Accion {
	/* TIPOS DE ACCIONES (MULTIK)
	 * HAPM: Hablar sobre actividad con profesor (niña)
	 * HAPH: Hablar sobre actividad con profesor (niño)
	 * 
	 * HAOM: Hablar sobre actividad con observador (niña)
	 * HAOH: Hablar sobre actividad con observador (niño)
	 * 
	 * HACM: Hablar sobre actividad con compañero (niña)
	 * HACH: Hablar sobre actividad con compañero (niño)
	 * 
	 * Siguiendo el mismo patron:
	 * HO: Hablar sobre otro tema
	 * M: Molestar a compañero
	 * DSD: Distraccion sin disrupcion
	 * */
	
	private String fechaHora;
	private String accion;

		
	public static final String ACCION="accion";
	public static final String FECHA_HORA="fecha";
	public String getFechaHora() {
		return fechaHora;
	}
	public void setFechaHora(String fechaHora) {
		this.fechaHora = fechaHora;
	}
	public String getAccion() {
		return accion;
	}
	public void setAccion(String accion) {
		this.accion = accion;
	}
	
	

}
